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
	#print(ser.readline())
	varx = ser.readline().decode('utf-8').replace(" ", "")
	varx = ser.readline().decode('utf-8').replace(":", "")
	if varx == "":
		continue
	else:
		if varx[0] == '1':
			dict[1] = varx[1] + varx[2]
			print(dict[1])
			r.table("sensor1").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '2':
			dict[2] = varx[1] + varx[2]
			print(dict[2])
			r.table("sensor2").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '3':
			dict[3] = varx[1] + varx[2]
			print(dict[3])
			r.table("sensor3").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '4':
			dict[4] = varx[1] + varx[2]
			print(dict[4])
			r.table("sensor4").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '5':
			dict[5] = varx[1] + varx[2]
			print(dict[5])
			r.table("sensor5").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '6':
			dict[6] = varx[1] + varx[2]
			print(dict[6])
			r.table("sensor6").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '7':
			dict[7] = varx[1] + varx[2]
			print(dict[7])
			r.table("sensor7").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '8':
			dict[8] = varx[1] + varx[2]
			print(dict[8])
			r.table("sensor8").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '9':
			dict[9] = varx[1] + varx[2]
			print(dict[9])
			r.table("sensor9").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		elif varx[0] == '10':
			dict[10] = varx[1] + varx[2]
			print(dict[10])
			r.table("sensor10").insert([{"Vochtigheid": varx[1] + varx[2], 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]).run(conn)
		else:
			continue
