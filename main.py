import convert
import time
from rich.prompt import Confirm
import saver
import printer
import gp
import device_output
from device_output import device
# Program disclaimer: Getting nmea protocol data, directly from the device and converts it to readable outputs


# sorts the data by the protocol type and converts it to a list, if it isn't already, 
#return "dont print" stands for all the protocols that are not needed
# returns a dict rdy to print
def sort(raw_data):
    if not isinstance(raw_data,  list):
        raw_data = convert.to_a_list(raw_data)
    for lines in raw_data:
        if lines[0] == '$GNRMC' or lines[0] == '$GPRMC':
            return dict(gp.rmc(lines))
        elif lines[0] == '$GPGGA':
            return dict(gp.gga(lines))
        elif lines[0] == '$GPGLL':
            return dict(gp.gll(lines))
        elif lines[0] == '$GNGSA' or lines[0] == '$GPGSA':
            return dict(gp.gsa(lines))
        else:
            return "dont print"
        break

# creates a dict that has all the relavent data from the last 12 protocols sended by the device
# returns a dict 
def summary():
    final_dict = {
        "Datum" : "", 
        "Zeit" : "",
        "Länge" : "", 
        "Breite" : "",
        "Höhe" : "",
        "Geschwindigkeit" : "",
        "Track angle" : "",
        "Status" : "",
        "GPS-Qualität" : "",
        "Anzahl Sattelieten" : "", 
        "PRN" : "",
        "HDOP" : "",
        "VDOP" : "",
        "Selection of 2D or 3D" : "",
        "3D fix" : "", 
    }
    # the loop is giving the device output as a str into the sort func and then saves it into a dict
    # the protocol has 6 lines, so in range(12) makes sure that it gets at least one line for the dict 
    for i in range(12):
        temp_dict = sort(dev.output_str())
        # merges the dicts if they are relevent !the last input into the dict overrides the previous data!
        if temp_dict != "dont print":
            final_dict = {**final_dict, **temp_dict}
        else:
            pass
    return dict(final_dict)

dev = device()
has_rich = Confirm.ask("Ist auf ihrem Gerät \"rich\" installiert?")
want_to_save = Confirm.ask("Wollen sie die Daten abspeichern?")
if want_to_save:
    want_to_save_raw = Confirm.ask("Auch die roh Daten?")
elif not want_to_save:
    want_to_save_raw = False
# the processing loop 
while True:
    sum_dict = dict(summary())
    if has_rich:
        printer.pretty_dict_print(dict(sum_dict))
    elif not has_rich:
        printer.dict_print(dict(sum_dict))

    # saves the raw device output and the convertet data, if the user confirmed it at the start
    if want_to_save_raw and want_to_save:
        raw_protocol = dev.output_str()
        saver.save_raw(raw_protocol)
        saver.save_summary(dict(sum_dict))
    elif want_to_save:
        saver.save(dict(sum_dict))
    else:
        pass


