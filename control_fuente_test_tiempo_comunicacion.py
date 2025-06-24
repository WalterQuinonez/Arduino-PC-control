# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 13:34:22 2025

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
current_read = []
current_read.append(["Measured Voltage","Programmed Voltage", 
                "Measured Current", "Programmed Current", 
                "Over Voltage" , "Set point" , "Under Voltage Set Point"] ) 

enviar_comando('ADR 6')
enviar_comando('IDN?')
enviar_comando('RMT 2')
enviar_comando('CLS')
enviar_comando('OUT 1') #prende y apaga la salida
   



'''PROBAR ESTO PRIMERO Y CHEQUEAR LOS TIEMPO DE LA COMUNICACION'''

vout = 3
tiempo = time.time()
enviar_comando(f'PV {vout}')
print(f'tiempo de comunicacion {time.time() - tiempo } segundos')
#loop para que el equipo me mande mediciones mientras completo el tiempo de aplicacion
#dada la velocidad de comunicación, pedir data en intervalos menores a 1 seg es al pedo
for i in range(5):
    tiempo = time.time()
    current_read.append(str(enviar_comando('DVC?')))
    print(f'tiempo de comunicacion {time.time() - tiempo } segundos')

    #time.sleep(tapp) #esto no se si es necesario, probrar primero sin usar esto
                      #el tema es que quizas este comando ya mete un segundo de delay
#Repito para el tiempo muerto
vout = 0
tiempo = time.time()
enviar_comando(f'PV {vout}')
print(f'tiempo de comunicacion {time.time() - tiempo } segundos')

for i in range(5):
    tiempo = time.time()
    current_read.append(str(enviar_comando('DVC?')))
    print(f'tiempo de comunicacion {time.time() - tiempo } segundos')


