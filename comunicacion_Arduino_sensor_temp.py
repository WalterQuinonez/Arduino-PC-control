# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 16:02:28 2025

@author: walte
"""

import serial
import serial.tools.list_ports
import time

# Obtener lista de puertos disponibles
puertos = serial.tools.list_ports.comports()

for puerto in puertos:
    print(f"Nombre: {puerto.device}")
    print(f"Descripción: {puerto.description}")
    print(f"HWID: {puerto.hwid}")
    print("-" * 30)



# Configurá el puerto y el baud rate
ser = serial.Serial('COM11', 9600)  # Cambiá 'COM3' por tu puerto (ej: '/dev/ttyUSB0' en Linux)
time.sleep(2)  # Espera a que se establezca la conexión

datos_temperatura = []
muestras = 0
puntos = 100

try:
    while muestras < puntos:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            try:
                temp = float(linea)
                datos_temperatura.append(linea)
                muestras += 1
                print(f"{muestras}. Temperatura: {linea} °C")
                #time.sleep(1)  # Esperar 1 segundo después de una lectura válida
            except ValueError:
                print(f"Dato no válido recibido: {linea}")
except KeyboardInterrupt:
    print("Lectura interrumpida por el usuario.")
finally:
    ser.close()
    print("Puerto cerrado.")    