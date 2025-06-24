# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 10:32:36 2025

@author: walte

Prueba: controlo arduino desde python usando comandos para que arranque la medicion 
y cuando termine o se corte arduino deje de leer. Hacer esto mejora la estabilidad 
y la sincronizacion entre arduino y la pc. Caso contrario en corridas sucesivas la 
compu se descincroniza y lee datos validos numericamente, pero que no son los correctos. 

El comando DELAYXXXX determina el delay entre mediciones de temperatura que va a hacer arduino. 
los numeros XXXX estan en milisengundos. Los valores tipicos estan entre 500 y 1000.

Como test de control puse una temperatura maxima, que si es excedida el programa se corta y 
arduino deja de medir. 
 

"""



import serial
import time

ser = serial.Serial('COM11', 9600, timeout=1)
time.sleep(2)  # dejar que Arduino reinicie
temperatura_maxima = 1000.0  # grados Celsius

ser.write(b'DELAY500\n')   # Enviar nuevo delay
ser.write(b'START\n')  # Inicia la medición

try:
    for i in range(500):
        tiempo = time.time()
        linea = ser.readline().decode().strip() #lee la temperatura de arduino
        duracion = time.time() - tiempo 
        
        if linea: #esto es true si es un dato valido, de lo contrario manda advertencia
            try:
                temperatura = float(linea) #convierte la data en float
                print(f"{i+1}. {temperatura} °C --- tiempo = {duracion:.3f} segundos")
                
                #condicion de corte de temperatura
                if temperatura > temperatura_maxima:
                    print(f"Temperatura crítica alcanzada: {temperatura} °C")
                    ser.write(b'STOP\n') #detiene la medicion
                    break  # Salir del bucle

            except ValueError:
                print(f"{i+1}. Dato no válido recibido: '{linea}'")
        
        
finally:
    ser.write(b'STOP\n')  # Detiene la medición
    ser.close()