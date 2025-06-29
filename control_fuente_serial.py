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


def aplicar_voltaje(v,tapp, toff ):
    
    current_read = []
    vout = 3
    enviar_comando(f'PV {vout}')
    #loop para que el equipo me mande mediciones mientras completo el tiempo de aplicacion
    #dada la velocidad de comunicación, pedir data en intervalos menores a 1 seg es al pedo
    for i in range(5):
        current_read.append(str(enviar_comando('DVC?')))
        #time.sleep(tapp) #esto no se si es necesario, probrar primero sin usar esto
                          #el tema es que quizas este comando ya mete un segundo de delay
    #Repito para el tiempo muerto
    vout = 0
    enviar_comando(f'PV {vout}')
    current_read.append(str(enviar_comando('DVC?')))
    for i in range(5):
        current_read.append(str(enviar_comando('DVC?')))

    return current_read
    
    

# Configuración del puerto serial
puerto = 'COM4' # Cambia &#39;COM3&#39; por el puerto serial que uses (ej.&#39;/dev/ttyUSB0&#39; en Linux)
baudrate = 9600
# Abrir conexión serial
ser = serial.Serial(puerto, baudrate, timeout=1)
#time.sleep(2) # Esperar a que se establezca la conexión
# Función para enviar comando y leer respuesta
current_read = []
current_read.append(["Measured Voltage","Programmed Voltage", 
                "Measured Current", "Programmed Current", 
                "Over Voltage" , "Set point" , "Under Voltage Set Point"] ) 

enviar_comando('ADR 6')
enviar_comando('IDN?')
enviar_comando('RMT 2')
enviar_comando('CLS')
enviar_comando('OUT 1') #prende y apaga la salida
   

voltaje = enviar_comando('PC 6') # con esto fijo la corriente de salida maxima
current_read = aplicar_voltaje(v,tapp, toff )    
