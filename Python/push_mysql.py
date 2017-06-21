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
import serial, string, time,re, sys, MySQLdb
from random import randint
from datetime import datetime

db = MySQLdb.connect(host="146.185.176.134",    # your host, usually localhost
                     user="root",               # your username
                     passwd="root",             # your password
                     db="Sensoren")             # name of the data base
cur = db.cursor()

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)

varx = ""
		
while True:
	varx = ser.readline().decode('utf-8').replace(" ", "")
	varx = ser.readline().decode('utf-8').replace(":", "")

	if varx == "" or varx[0] == '0':
		continue
	else:
		try:
			if len(varx) == 4:
				print varx[0], varx[1]
				cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (%s,%s) """,(varx[0], varx[1]))
				db.commit()
			elif len(varx) == 5:
				print varx[0], varx[1] + varx[2]
				cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (%s,%s) """,(varx[0], varx[1] + varx[2]))
				db.commit()
		except:
			continue
