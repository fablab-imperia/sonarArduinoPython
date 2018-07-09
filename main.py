#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:30:52 2018

@author: rosto
"""
import sys
try:
    import serial
except ImportError:
    print("Libreria pySerial non trovata")
    sys.exit()

try:
    import PyGnuplot as gp
except ImportError:
    print("Libreria PyGnuplot non trovata")
    sys.exit()

try:
    import easygui
except ImportError:
    print("Libreria easygui non trovata")
    sys.exit()

import math##già nelle librerie standard
import time


#Arduino seriale
port= easygui.enterbox("Inserisci il percorso per la porta Arduino, tipicamente /dev/ttyACM*")
if (port == None or port == ''):
    print("Inserire una porta valida")
ard = serial.Serial(port,9600,timeout=5)

#Tipo di grafico
#tipoDiGrafico = easygui.buttonbox("Seleziona come vuoi che vengano mostrati i dati", choices=["Grafico radiale","Cartesiano r in funzione di teta"])
#if tipoDiGrafico==None or tipoDiGrafico=="Cartesiano r in funzione di teta":
#    tipoDiGrafico="cartesiano"
#else:
#    tipoDiGrafico="radiale"
#
##Modalita specchio
#modalitaSpecchio = easygui.buttonbox("Attivare modalità specchio?", choices=["Sì","No"])
#if modalitaSpecchio=="Sì":
#    modalitaSpecchio=True
#else:
#    modalitaSpecchio=False

#Grafico
dizDati={}
#plt.hold(False)

ard.flush()
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
       
    x=[]
    y=[]
#    if (tipoDiGrafico=="radiale"):
#        for i in range(len(valoriRaggi)):
#            x.append(valoriRaggi[i]*math.cos(sorted(dizDati.keys())[i]*math.pi/180.0))
#            y.append(valoriRaggi[i]*math.sin(sorted(dizDati.keys())[i]*math.pi/180.0))
#    else:##Cartesiano ro-teta
#        x = sorted(dizDati.keys())
#        y = valoriRaggi
#        
#    if modalitaSpecchio:
#        for i in range(len(x)):
#            x[i]=-x[i]
#        y.reverse()
    x = sorted(dizDati.keys())
    y = valoriRaggi
    
    #file temporaneo
    f = open("temp.dat","w")
    for ang in sorted(dizDati.keys()):
        f.write(str(ang)+" "+str(dizDati[ang]))
    f.close
    
    ##Disegno vero e proprio del grafico
    gp.c("plot 'temp.dat' using 1:2 with lines")
    time.sleep(0.05)