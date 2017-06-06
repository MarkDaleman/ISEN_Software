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

dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
varx = ""
while True:
	#print(ser.readline())
	varx = ser.readline().decode('utf-8').replace(" ", "")
	varx = ser.readline().decode('utf-8').replace(":", "")
	if varx == "":
		continue
	else:
		if varx[0] == '1':
			dict[1] = varx[1] + varx[2]
			print(dict[1])
		elif varx[0] == '2':
			dict[2] = varx[1] + varx[2]
			print(dict[2])
		elif varx[0] == '3':
			dict[3] = varx[1] + varx[2]
			print(dict[3])
		elif varx[0] == '4':
			dict[4] = varx[1] + varx[2]
			print(dict[4])
		elif varx[0] == '5':
			dict[5] = varx[1] + varx[2]
			print(dict[5])
		elif varx[0] == '6':
			dict[6] = varx[1] + varx[2]
			print(dict[6])
		elif varx[0] == '7':
			dict[7] = varx[1] + varx[2]
			print(dict[7])
		elif varx[0] == '8':
			dict[8] = varx[1] + varx[2]
			print(dict[8])
		elif varx[0] == '9':
			dict[9] = varx[1] + varx[2]
			print(dict[9])
		elif varx[0] == '10':
			dict[10] = varx[1] + varx[2]
			print(dict[10])
		else:
			continue
