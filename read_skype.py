import sqlite3 as lite
import sys
import os
import time
import getpass
USER = getpass.getuser()
USERNAME = sys.argv[1]
maxid = 0

while True:
    con = None
    try:
        con = lite.connect('/home/{0}/.Skype/{1}/main.db'.format(USER, USERNAME))
        last_item = con.execute('SELECT max(id) from Messages')
        for item in last_item:
            if maxid < item[0]:
                maxid = item[0]

                cursor = con.execute('SELECT from_dispname, body_xml from Messages where id = (SELECT max(id) from Messages)')
                
                for row in cursor:
                    print row[0], row[1]
                    os.system('milena_say "{0} {1}"'.format(row[0].encode("utf-8"),row[1].encode("utf-8")))    
        
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:
        if con:
            con.close()

