# gets the data and backs it up in a text file

def save(dic):
    file = open("data.txt", "a")
    for keys,values in dic.items():
        if isinstance(values, str):
            file.write(f"{keys} : {values}\n")
        else:
            file.write(f"{keys} : /\n")
    file.close()

def save_raw(data):
    file = open("raw_data.txt", "a")
    file.write(f"{data}")
    file.close()

def save_summary(dic):
    file = open("summary_data.txt", "a")
    for keys,values in dic.items():
        if isinstance(values, str):
            file.write(f"{keys} : {values}\n")
        else:
            file.write(f"{keys} : /\n")
    file.close()