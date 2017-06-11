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

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)

varx = ""

while True:
	varx = ser.readline().decode('utf-8').replace(" ", "")
	varx = ser.readline().decode('utf-8').replace(":", "")
	if varx == "":
		continue
        datumCheck()
	else:
		cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (%s,%s) """,(varx[0], varx[1] + varx[2]))
        datumCheck()

def datumCheck():
    cmd = "SELECT * FROM Planten"
    try:
        # Execute the SQL command
        cur.execute(cmd)
        # Fetch all the rows in a list of lists.
        results = cur.fetchall()
        for row in results:
            timestamp = row[3]
        #   print "timestamp: %s" % (timestamp)
        #   print "TIMESTAMP: " + now
            if timestamp < datetime.datetime.now()-datetime.timedelta(days=365):
                verwijder = "DELETE FROM Planten WHERE timestamp = '%s'" % (timestamp)
                print "Record is ouder dan een jaar, wordt verwijdert."
                cur.execute(verwijder)
            else:
                print "Record is nog geen jaar, blijft bewaard."
    except e:
       print e
