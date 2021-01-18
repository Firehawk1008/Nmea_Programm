import convert
import gp
import device_output
from device_output import device
# Program disclaimer: Getting nmea protocol data, directly from the device and converts it to readable outputs


# sorts the data by the protocol type and converts it to a list, if it isn't already
# returns None
def sort(raw_data):
    if not isinstance(raw_data,  list):
        raw_data = convert.to_a_list(raw_data)
    for lines in raw_data:
        if lines[0] == '$GNRMC' or lines[0] == '$GPRMC':
            gp.rmc(lines)
        elif lines[0] == '$GPZDA':
            break
        elif lines[0] == '$GPGGA':
            gp.gga(lines)
        elif lines[0] == '$GPGLL':
            break
        elif lines[0] == '$GPVTG':
            break
        elif lines[0] == '$GNGSA' or lines[0] == '$GPGSA':
            gp.gsa(lines)
        elif lines[0] == '$GPGSV':
            break
        elif lines[0] == '$GLGSV':
            break
        else:
            print(lines)

i = device()
while True:
    sort(i.output_str())



