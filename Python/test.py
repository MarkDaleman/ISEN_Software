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
import serial, string, time,re, sys
from random import randint
import rethinkdb as r
from datetime import datetime

conn = r.connect(host='146.185.180.205', port=28015, db='Sensoren')

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)

dict = {0:'0', 1:'0', 2:'0', 3:'0', 4:'0', 5:'0', 6:'0', 7:'0', 8:'0', 9:'0', 10:'0'}
varx = ""

while True:
	print(ser.readline())
	varx = ser.readline().decode('utf-8').replace(" ", "")
	varx = ser.readline().decode('utf-8').replace(":", "")
	if varx == "":
		continue
	else:
		print(ser.readline())
