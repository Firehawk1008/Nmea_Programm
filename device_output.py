import serial
import os
import sys
import subprocess
import time
from serial import Serial

# class for getting the serial nmea-data from the device
class device(object):
    def __init__(self):
        if os.geteuid() == 0:
            pass
        # sudo rights are needed to use the serial input
        else:
            subprocess.call(['sudo', 'python3', *sys.argv])
            sys.exit()
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)
        except Exception as err:
            print("Bitte überprüfen sie ob ihr Gerät angeschlossen ist. \nVersuchen sie es anschließend erneut.")
            quit()
            

    # returns the output from the device in a single line as bytes
    def output(self):
        return self.ser.readline()

    # returns the output from the device in a single line as a string
    def output_str(self):
        return str(self.ser.readline(), "utf-8")