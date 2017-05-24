'''
Python Drivers: https://www.rethinkdb.com/docs/install-drivers/
URL van de Server: 146.185.180.205
Webpanel: 146.185.180.205:8080
'''
from random import randint
import rethinkdb as r
from datetime import datetime
conn = r.connect(host='146.185.180.205',
                 port=28015,
                 db='testMark')

y = 0
while y < 100:
    x = randint(0, 100)
    r.table("Sensoren").insert([{
            "sensorID": "1",
            "Vochtigheid": x,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }]).run(conn)
    y +=1





print("Aantal items in de Database", r.table('Sensoren').count().run(conn))
print("Aantal items in de Database waar vochtigheid > 50", r.table('Sensoren')['Vochtigheid'].count(lambda Vochtigheid: Vochtigheid > 50).run(conn))
print("Aantal items in de Database waar vochtigheid < 50", r.table('Sensoren')['Vochtigheid'].count(lambda Vochtigheid: Vochtigheid < 50).run(conn))
print("Aantal items in de Database waar vochtigheid == 50", r.table('Sensoren')['Vochtigheid'].count(lambda Vochtigheid: Vochtigheid == 50).run(conn))
print("Alle vochtigheid bij elkaar opgeteld", r.table('Sensoren')['Vochtigheid'].count(lambda Vochtigheid: Vochtigheid + Vochtigheid).run(conn))

#Table aanmaken in ISEN DB
#r.db("ISEN").table_create("Sensoren").run()

#Data toevoegen aan data
r.db("ISEN").table('Sensoren').filter({"id": "1"})

#r.db("ISEN").table("Sensoren").insert([{ "id": "1", "sensorID": "1", "Vochtigheid": "99"}]).run()

