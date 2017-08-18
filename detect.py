#!/usr/bin/env python3

from ard_core import *
import serial

with serial.Serial(find_port(), 9600) as ser:
#    ser.write(1)
    while True:
        data = ser.readline()
        number = int(data.decode("utf-8").strip())
        print("Received: {}".format(number))
        if number >= 0:
            number = (number + 1) % 128
            print("Writing: {}".format(number))
            ser.write(bytearray([number]))
