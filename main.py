import convert
from rich.prompt import Confirm
import saver1
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
        elif lines[0] == '$GPZDA':
            break
        elif lines[0] == '$GPGGA':
            return dict(gp.gga(lines))
        elif lines[0] == '$GPGLL':
            break
        elif lines[0] == '$GPVTG':
            break
        elif lines[0] == '$GNGSA' or lines[0] == '$GPGSA':
            return dict(gp.gsa(lines))
        elif lines[0] == '$GPGSV':
            break
        elif lines[0] == '$GLGSV':
            break
        else:
            break
    return ""

i = device()
want_to_save = Confirm.ask("Wollen sie die Daten abspeichern?")
while True:
    raw_protocol= i.output_str()
    dic = sort(raw_protocol)
    printer.dic_print(dict(dic))

    # saves the raw device output and the convertet data, if the user confirmed it at the start
    if want_to_save == True:
        saver1.save_raw(raw_protocol)
        saver1.save(dict(dic))



