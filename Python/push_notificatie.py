from urllib2 import *
import urllib
import json
import sys
import MySQLdb

API_KEY="AIzaSyBOTaWUvzwtWHfEpZ8zH8d-31aKZn6k4Po"

db = MySQLdb.connect(host="146.185.176.134",    # your host, usually localhost
                     user="root",               # your username
                     passwd="root",             # your password
                     db="Sensoren")             # name of the data base

cur = db.cursor()

sql_cmd = "SELECT t1.plantid, t1.moisture, t1.timestamp, t3.plantNaam \
            FROM Planten t1 JOIN (SELECT plantNaam, plantid FROM PlantNamen) as t3 \
            ON t1.plantid = t3.plantid \
            JOIN (SELECT plantid, MAX(timestamp) timestamp \
            FROM Planten GROUP BY plantid) as t2 ON t1.plantid = t2.plantid \
            AND t1.timestamp = t2.timestamp ORDER BY t1.plantid"
cur.execute(sql_cmd)
results = cur.fetchall()

def sendBericht(messageTitle, messageBody):
    data={
        "to" : "/topics/my_little_topic",
        "notification" : {
            "body" : messageBody,
            "title" : messageTitle,
            "icon" : "ic_cloud_white_48dp"
        }
    }

    dataAsJSON = json.dumps(data)

    request = Request(
        "https://gcm-http.googleapis.com/gcm/send",
        dataAsJSON,
        { "Authorization" : "key="+API_KEY,
          "Content-type" : "application/json"
        }
    )

    print urlopen(request).read()

for row in results:
    plantid = row[0]
    moisture = row[1]
    #print "id: %s" % (plantid) + " moisture: %s" % (moisture)
    if moisture < '35':
        sendBericht("Plant %s" % (plantid) + " heeft weinig water.", "Er zal binnenkort automatisch water worden gegeven.")
