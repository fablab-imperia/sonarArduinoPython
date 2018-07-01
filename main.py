#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:30:52 2018

@author: rosto
"""

import serial
import matplotlib.pyplot as plt

dizDati={}

port=str(input("Inserire percorso interfaccia: "))
ard = serial.Serial(port,9600,timeout=5)
ard.flush()
while True:
    msg = ard.readline()
    msg.translate(None ,b'\r\n')
    msg = msg.decode("utf-8")
    if msg.count("-")==1:
#        print(msg)
        angolo, distanza = msg.split("-")
#        print(type(angolo))
        distanza=distanza.replace("\r\n","")
        angolo= int(angolo)
        distanza=float(distanza)
        dizDati[angolo]=distanza
        print("Angolo "+str(angolo)+", distanza "+str(distanza))
    else:
        pass
    valoriRaggi = []
    for ang in sorted(dizDati.keys()):
        valoriRaggi.append(dizDati[ang])
    plt.plot(sorted(dizDati.keys()), valoriRaggi)
    
    plt.show()