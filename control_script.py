# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 00:37:23 2025

@author: walte
"""

import serial
import time

# Cambia el puerto COM por el tuyo (ej. "COM3" en Windows o "/dev/ttyUSB0" en Linux)
puerto = 'COM6'
arduino = serial.Serial(puerto, 9600, timeout=1)
time.sleep(2)  # Espera a que el Arduino se reinicie al conectarse

# Envía la señal de inicio
arduino.write(b'START\n')
print("Comando 'START' enviado al Arduino.")
# Leer respuesta (opcional)
respuesta = arduino.readline().decode().strip()
print("Respuesta del Arduino:", respuesta)



# Envía la señal de inicio
arduino.write(b'STOP\n')
print("Comando 'STOP' enviado al Arduino.")
respuesta = arduino.readline().decode().strip()
print("Respuesta del Arduino:", respuesta)

arduino.close()
