def datumCheck():
    cmd = "SELECT * FROM Planten"
    try:
        # SQL uitvoeren
        cur.execute(cmd)
        # Alles ophalen
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
       
