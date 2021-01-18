import convert
import printer

# gets the raw gpgga data as an array/list and converts it to an dictonary with readable outputs
# returns the dictonary
def gga(gpgga_data):
    gpgga_data.pop(0)
    
    print("GPGGA:")
    gga_data = {
        "Zeit" : convert.time(gpgga_data[0]) , 
        "Breite" : convert.coordinate(gpgga_data[1], gpgga_data[2]) ,
        "Länge" : convert.coordinate(gpgga_data[3], gpgga_data[4]) ,
        "GPS-Qualität" : convert.gps_quality(gpgga_data[5]) ,
        "Anzahl Sattelieten" : gpgga_data[6] ,
        "Horizontal Dilution of Precision (HDOP)" : gpgga_data[7] ,
        "Höhe" : gpgga_data[8] ,
    #    "Höhendifferenz zwischen Ellipsoid und Geoid" : ""
    }
    printer.dic_print(gga_data)

def gsa(gpgsa_data):
    gpgsa_data.pop(0)

    print("GPGSA:")
    gsa_data = {
        "Selection of 2D or 3D" : gpgsa_data[0],
        "3D fix" : gpgsa_data[1],
        "PRN" : convert.prn(gpgsa_data),
        "PDOP" : gpgsa_data[-4],
        "HDOP" : gpgsa_data[-3],
        "VDOP" : gpgsa_data[-2],
    }
    printer.dic_print(gsa_data)

def rmc(gprmc_data):
    gprmc_data.pop(0)

    print("GPRMC")
    rmc_data = {
        "Zeit" : convert.time(gprmc_data[0]) ,
        "Status" : convert.status(gprmc_data[1]) ,
        "Breite" : convert.coordinate(gprmc_data[2], gprmc_data[3]) ,
        "Länge" : convert.coordinate(gprmc_data[4], gprmc_data[5]) ,
        "Geschwindigkeit" : convert.speed(gprmc_data[6]),
        "Track angle" : f"{gprmc_data[7]}°", 
        "Datum" : convert.date(gprmc_data[8]) ,
        "Magnetische Vari." : f"{gprmc_data[9]}, W"
    }

    printer.dic_print(rmc_data)