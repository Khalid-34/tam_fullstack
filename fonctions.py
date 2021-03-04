import sqlite3
import os
import sys
from back import main


def next_trip(station):
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.execute("""SELECT route_short_name, stop_name, trip_headsign, timeline FROM infoarret WHERE stop_name=?""",(station))
    #for ligne in c.fetchall():
    return c.fetchall()

print(next_trip("COMEDIE"))





# if name == "main":
#     sys.exit(main())

