#!/usr/bin/python
import MySQLdb, datetime
from datetime import timedelta

db = MySQLdb.connect(host="146.185.176.134",    # your host, usually localhost
                     user="root",               # your username
                     passwd="root",             # your password
                     db="Sensoren")             # name of the data base

cur = db.cursor()

vocht = '66'
planttid = 6

cur.execute("INSERT INTO PlantenTest (plantid, moisture) VALUES (4, '55')")
cur.execute("INSERT INTO PlantenTest (plantid, moisture) VALUES (2, '76')")
cur.execute("INSERT INTO PlantenTest (plantid, moisture) VALUES (1, '33')")
cur.execute("INSERT INTO PlantenTest (plantid, moisture) VALUES (1, '60')")

cur.execute("INSERT INTO PlantenTest (plantid, moisture) VALUES (%s,%s) """,(planttid, vocht))

# cmd = "SELECT * FROM Planten"
#
#
# try:
#     # Execute the SQL command
#     cur.execute(cmd)
#     # Fetch all the rows in a list of lists.
#     results = cur.fetchall()
#     for row in results:
#         timestamp = row[3]
#     #   print "timestamp: %s" % (timestamp)
#     #   print "TIMESTAMP: " + now
#         if timestamp < datetime.datetime.now()-datetime.timedelta(seconds=10):
#             verwijder = "DELETE FROM Planten WHERE timestamp = '%s'" % (timestamp)
#             print "ouder dan een jaar"
#             cur.execute(verwijder)
#         else:
#             print "jonger dan een jaar"
# except e:
#    print e


# for row in cur.fetchall():
#     print row[0]
#     print row[1]
#     print row[2]

db.commit()
db.close()
