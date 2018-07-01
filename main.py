#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:30:52 2018

@author: rosto
"""

import serial

port=str(input("Inserire percorso intrerfaccia: "))

ard = serial.Serial(port,9600,timeout=5)

while True:
    ard.flush()
    msg = str(ard.readline())
    msg = msg.replace("b'", "")
    msg = msg.rstrip()
    try:
        angolo, distanza = msg.split("-")
        angolo= float(angolo)
        distanza=float(distanza)
        distanza = distanza.rstrip()
    except:
        pass
    
    print("Angolo: "+angolo+", distanza: "+distanza)