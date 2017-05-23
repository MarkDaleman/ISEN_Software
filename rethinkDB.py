'''
Python Drivers: https://www.rethinkdb.com/docs/install-drivers/
URL van de Server: 146.185.180.205
Webpanel: 146.185.180.205:8080
'''

import rethinkdb as r
r.connect('146.185.180.205', 28015).repl()

#Table aanmaken in ISEN DB
#r.db("ISEN").table_create("Sensoren").run()

#Data toevoegen aan data
r.db("ISEN").table('Sensoren').filter({"id": "1"})

#r.db("ISEN").table("Sensoren").insert([{ "id": "1", "sensorID": "1", "Vochtigheid": "99"}]).run()
