'''
Python Drivers: https://www.rethinkdb.com/docs/install-drivers/
URL van de Server: 146.185.180.205
Webpanel: 146.185.180.205:8080
'''

import rethinkdb as r
r.connect('146.185.180.205', 28015).repl()

r.table('tv_shows').insert({ 'name': 'bassie en adriaan' }).run()