#!/usr/bin/env python3

import serial.tools.list_ports

def find_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if int(p.pid) == 29987:
            return p.device

with serial.Serial(find_port(), 9600, timeout=1) as ser:
    
    
