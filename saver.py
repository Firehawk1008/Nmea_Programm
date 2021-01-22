from datetime import datetime
# gets the data and backs it up in a text file

def save_raw(data):
    file = open("raw_data.txt", "a")
    file.write(f"{data}")
    file.close()

def save_summary(dic):
    file = open("data.txt", "a")
    for keys,values in dic.items():
        if isinstance(values, str):
            file.write(f"{keys} : {values}\n")
        else:
            file.write(f"{keys} : /\n")
    file.close()

def time_stamp():
    file = open("data.txt", "a")
    date = datetime.now().strftime("%d-%m-%y, %H:%M:%S")
    file.write(f"{date}\n")
    file.close()

def time_stamp_raw():
    file = open("raw_data.txt", "a")
    date = datetime.now().strftime("%d-%m-%y, %H:%M:%S")
    file.write(f"{date}\n")
    file.close()