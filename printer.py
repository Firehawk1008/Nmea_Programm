import rich

def dic_print(dic):
    for keys,values in dic.items():
        if isinstance(values, str):
            print (f"{keys} : {values}")
        else:
            print (f"{keys} : /")
    print("")