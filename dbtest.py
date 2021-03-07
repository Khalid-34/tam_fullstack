import sqlite3
import logging
import random
import urllib.request
import csv

logging.basicConfig(level=logging.DEBUG)


db = sqlite3.connect(":memory:")

db.set_trace_callback(logging.debug)

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS "infoarret" (
    "stop_name"	TEXT,
    "route_short_name"	TEXT,
    "trip_headsign"	TEXT,
    "timeline" TEXT,
    "delay_sec"	INTEGER
    );""")

def load_csv(path, cursor):

    """Cette fonction se charge de remplir la table 'infoarret'"""
    
    with open(path, "r") as f:
        f.readline()
        line = f.readline()
        while line:
            insert_csv_row(line, cursor)
            line = f.readline()


load_csv('tam.csv', cur)

# a,b,c,d,e = random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)

new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], liste_row[9]]

# cur.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """, (a,b,c,d,e))
cur.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
                    new_row)


