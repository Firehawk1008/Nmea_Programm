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
        else:
            print("Bitte gib das Rootpasswort ein")
            subprocess.call(['sudo', 'python3', *sys.argv])
            sys.exit()

        self.ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)

    # returns the output from the device in a single line as bytes
    def output(self):
        return self.ser.readline()

    # returns the output from the device in a single line as a string
    def output_str(self):
        return str(self.ser.readline(), "utf-8")