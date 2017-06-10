#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="146.185.176.134",    # your host, usually localhost
                     user="root",               # your username
                     passwd="root",             # your password
                     db="Sensoren")             # name of the data base

cur = db.cursor()

vocht = '44'

cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (4, vocht)")
# cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (2, '76')")
# cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (1, '33')")
# cur.execute("INSERT INTO Planten (plantid, moisture) VALUES (1, '60')")

# INSERT INTO user (companyName,user,pass,imei, checkPoint,licenceDate) VALUES (%s,%s,%s,%s,%s,%s) """,(companyname,username, password,imei,tval,currdate))


# for row in cur.fetchall():
#     print row[0]
#     print row[1]
#     print row[2]

db.commit()
db.close()
