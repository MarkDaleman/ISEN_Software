#!/usr/bin/python
"""
Python 3 code
Geschreven door Mark & Clemens
ISEN Minor Project

Ontvanger (Arduino Nano)
GRD  : GRD
VCC  : 5V
DATA : D12
USB  : Raspberry Pi

"""
import serial, string, time,re
import sys

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)

list = []
varx = ""
while True:
	#print(ser.readline())

	varx = ser.readline().decode('utf-8').replace(":", "")
	if varx == "":
		continue
	else:
		sys.stdout.write(varx)
		list.append(varx.rstrip())
		print(list)
