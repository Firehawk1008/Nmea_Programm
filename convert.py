# gets the not seperatet time and converts it to a user friendly time
# returns readable time as a str
def time(raw_time):
    return f"{raw_time[:2]}:{raw_time[2:4]}:{raw_time[4:6]} UTC"

# gets the not seperatet coordiate and converts it to a user friendly coordinate
# returns readable coordiantes as a str
def coordinate(raw_coordinate, direction):
    if direction == 'W' or direction == 'E':
        return raw_coordinate[1:3] + "d " + raw_coordinate[3:10] + "' " + direction
    elif direction == 'N' or direction == 'S':
        return raw_coordinate[0:2] + "d " + raw_coordinate[2:9] + "' " + direction

# gets the gps data
# returns a proper message for it, so the user can understand it better
def gps_quality(raw_data):
    if raw_data == '0':
        return 'Kein Signal'
    elif raw_data == '1':
        return 'Verbunden mit GPS'
    elif raw_data == '2':
        return 'Verbunden mit DGPS'

# gets a line from the protocol if its not a str it gets converted to one
# returns the data it got as a list wich is divided into useable chunks 
def to_a_list(raw_data):
    if isinstance(raw_data, str):
        arr = []
        arr.append(raw_data.strip().split(","))
        return arr
    elif not isinstance(raw_data, str):
        raw_data = str(raw_data, "utf-8")
        arr = []
        arr.append(raw_data.strip().split(","))
        return arr
    return None

# returns the same data as a str
def to_str(raw_data):
    if isinstance(raw_data, str):
        return raw_data
    else: 
        return str(raw_data, "utf-8")

# returns the prn data as an appended strs
def prn(raw_data):
    prn_data = f"{raw_data[2]}"
    for i in range(len(raw_data) - 7):
        prn_data += f", {raw_data[3+i]}"
    return prn_data

# returns the status as a Word/str
def status(raw_data):
    if raw_data == 'A':
        return "Active"
    elif raw_data == 'V':
        return "Void"
    else:
        return "Unknown"

#gets the speed as knots and converts it to km/h
#returns the speed in km/h as a str
def speed(raw_data):
    raw_data = float(raw_data)
    return str(round(raw_data * 1.852, 4)) + " km/h"

# returns the date as an readable str
def date(raw_date):
    return f"{raw_date[:2]}.{raw_date[2:4]}.20{raw_date[4:6]}"    

# returns the whole word for the selection for satelites
def selection(raw_selection):
    if raw_selection == "A":
        return "Auto"
    elif raw_selection == "M":
        return "Manual"