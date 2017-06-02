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
dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
varx = ""
while True:
	#print(ser.readline())

	varx = ser.readline().decode('utf-8').replace(" ", "")
	if varx == "":
		continue
	else:
		if varx[0] == '5':
			dict[5] = varx[1] + varx[2]
			print(dict[5])
		else:
			continue
