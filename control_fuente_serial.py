# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 13:30:03 2025

@author: walte
"""

import serial
import time


def enviar_comando(comando):
    comando_full = comando + '\r\n' # Algunos dispositivos requieren fin de línea CR+LF
    ser.write(comando_full.encode('utf-8')) # Enviar comando
    time.sleep(0.1) # Esperar respuesta
    respuesta = ser.readline().decode('utf-8').strip()
    return respuesta
    

# Configuración del puerto serial
puerto = 'COM4' # Cambia &#39;COM3&#39; por el puerto serial que uses (ej.&#39;/dev/ttyUSB0&#39; en Linux)
baudrate = 9600
# Abrir conexión serial
ser = serial.Serial(puerto, baudrate, timeout=1)
#time.sleep(2) # Esperar a que se establezca la conexión
# Función para enviar comando y leer respuesta

enviar_comando('ADR 6')
enviar_comando('RMT 2')
enviar_comando('CLS')
enviar_comando('OUT 1') #prende y apaga la salida

enviar_comando('IDN?')
    
    
voltaje = enviar_comando('PC 6') # con esto fijo la corriente de salida maxima

vouts = [0,0.5,1,1.5,2,2.5,3,2.5,2,1.5,1,0.5,0]
current_read = []
current_read.append(["Measured Voltage","Programmed Voltage", 
                "Measured Current", "Programmed Current", 
                "Over Voltage" , "Set point" , "Under Voltage Set Point"] ) 
for vout in vouts :
    # Ejemplo: solicitar voltaje de salida
    enviar_comando(f'PV {vout}')
    time.sleep(0.5)
    current_read.append(str(enviar_comando('DVC?')))
    time.sleep(0.5)


