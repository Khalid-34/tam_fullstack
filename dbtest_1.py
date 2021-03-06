import sqlite3
import logging
import urllib.request
import csv


logging.basicConfig(level=logging.DEBUG)


def update_db(csvurl, nom_csv):
    """Cette fonction telecharge le csv"""
    urllib.request.urlretrieve(csvurl, nom_csv)

def create_schema(cursor):
    """Cette fonction sert a créer la table 'infoarret' si inexistante"""
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS "infoarret" (
    "stop_name"	TEXT,
    "route_short_name"	TEXT,
    "trip_headsign"	TEXT,
    "timeline" TEXT,
    "delay_sec" INTEGER
    );""")

def insert_csv_row(csv_row, cursor):
    """Cette fonction sert a ajouter une ligne dans la DB"""
    liste_row = csv_row.strip().split(";")
    new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[7], liste_row[9]]
    cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """,
                    new_row)

def load_csv(path, cursor):
    """Cette fonction se charge de remplir la table 'infoarret'"""
    
    with open(path, "r") as f:
        f.readline()
        line = f.readline()
        while line:
            insert_csv_row(line, cursor)
            line = f.readline()

update_db('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv', 'tam.csv')


db = sqlite3.connect(":memory:")

db.set_trace_callback(logging.debug)

cur = db.cursor()


create_schema(cur)

load_csv('tam.csv',cur)

