import convert
import time
from rich.prompt import Confirm
import saver
import printer
import gp
import device_output
from device_output import device
# Program disclaimer: Getting nmea protocol data, directly from the device and converts it to readable outputs


# sorts the data by the protocol type and converts it to a list, if it isn't already
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

def summary():
    final_dic = {
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
    for i in range(12):
        temp_dic = sort(d.output_str())
        if temp_dic != "dont print":
            final_dic = {**final_dic, **temp_dic}
        else:
            pass
    return dict(final_dic)

d = device()
want_summary = Confirm.ask("Wollen sie die Daten zusammengefasst?")
want_to_save = Confirm.ask("Wollen sie die Daten abspeichern?")
while True:
    if want_summary == False:
        raw_protocol= d.output_str()
        dic = sort(raw_protocol)
        if dic == "dont print":
            pass
        else:
            printer.dic_print(dict(dic))
    else: 
        sum_dic = dict(summary())
        printer.pretty_dic_print(dict(sum_dic))

    # saves the raw device output and the convertet data, if the user confirmed it at the start
    if want_to_save and not want_summary:
        saver.save_raw(raw_protocol)
        saver.save(dict(dic))
    elif want_to_save and want_summary:
        saver.save(dict(sum_dic))


