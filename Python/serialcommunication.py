#!/usr/bin/python
"""
Python 3 code
Geschreven door Mark & Clemens
ISEN Minor Project
"""
import serial, string, time,re

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)


varx = ""
while True:
	#print(ser.readline())
	varx = ser.readline().decode('utf-8').replace(":", "")
	print(varx)