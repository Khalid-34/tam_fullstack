import csv
import sqlite3
import sys
import urllib.request
import os
import requests

# csv_url = 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
# with requests.Session() as s:
#     download = s.get(csv_url)

#     decoded_content = download.content.decode('utf-8')

#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
def update_db(csvurl, nom_csv):
    urllib.request.urlretrieve(csvurl, nom_csv)

        

def clear_rows(cursor):
    """Cette fonction efface le contenu de 'infoarret'"""
    
    cursor.execute("""DELETE FROM infoarret""")


def insert_csv_row(csv_row, cursor):
    """Cette fonction sert a ajouter une ligne dans la DB"""
    liste_row = csv_row.strip().split(";")
    new_row = [liste_row[4], liste_row[3], liste_row[7], liste_row[5], liste_row[9]]
    cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?,?) """, new_row)

def load_csv(path, cursor):
    """Cette fonction se charge de remplir la table 'infoarret'"""
    
    with open(path, "r") as f:
        f.readline()
        line = f.readline()
        while line:
            insert_csv_row(line, cursor)
            line = f.readline()
    

def remove_table(cursor):
    """Cette fonction supprime la table 'infoarret'"""
    
    cursor.execute("""DROP TABLE infoarret""")


def create_schema(cursor):
    """Cette fonction sert a créer la table 'infoarret' si inexistante"""
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS "infoarret" (
    "LIGNE"	TEXT,
    "ARRET"	TEXT,
    "HORAIRE" TEXT,
    "DESTINATION"	TEXT,
    "ATTENTE" INTEGER
    );""")


def main():
    update_db('https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv', 'tam.csv')
    conn=sqlite3.connect("trans_port.db")
    c=conn.cursor()
    create_schema(c)
    load_csv('tam.csv',c)
    conn.commit()
    conn.close()

    




if __name__ == "__main__":
    sys.exit(main())
    
