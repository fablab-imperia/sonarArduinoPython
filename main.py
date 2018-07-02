#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:30:52 2018

@author: rosto
"""

import serial
import matplotlib.pyplot as plt
import easygui

#Arduino seriale
port= easygui.enterbox("Inserisci il percorso per la porta Arduino, tipicamente /dev/ttyACM*")
if (port == None or port == ''):
    print("Inserire una porta valida")

ard = serial.Serial(port,9600,timeout=5)

ard.flush()

##Grafico
dizDati={}
plt.ion()
fig=plt.figure()
ax=fig.add_subplot(111)

#Ciclo principale
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
    ax.clear()
    ax.plot(sorted(dizDati.keys()), valoriRaggi)