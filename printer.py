from rich.console import Console
from rich.table import Table

def dict_print(dic):
    for keys,values in dic.items():
        if isinstance(values, str):
            print (f"{keys} : {values}")
        else:
            print (f"{keys} : /")
    print("")

def pretty_dict_print(dic):
    table = Table(title="NMEA-Daten")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    for keys,values in dic.items():
        if isinstance(values, str):
            table.add_row(keys, values)
        else:
            table.add_row(keys, "No Value")
    console = Console()
    console.print(table)


