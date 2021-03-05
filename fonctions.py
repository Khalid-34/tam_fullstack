import sqlite3
import os
import sys
from back import main
from time import *


def convertor(horaire):
    strftime('%M min %S sec', gmtime(horaire))
    return strftime('%M min %S sec', gmtime(horaire))


def all_lines():
    res={}
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.execute("""SELECT DISTINCT route_short_name, stop_name, trip_headsign FROM infoarret""")
    for ligne in c.fetchall():
        res.append(ligne)
    return res


def next_tram(line, station, direction): 
    res = {}   
    baseDeDonnees = sqlite3.connect('trans_port.db')
    curseur = baseDeDonnees.cursor()
    curseur.execute(" SELECT * FROM infoarret WHERE route_short_name = ? AND stop_name = ? AND trip_headsign = ? ",(line, station, direction))
    result = curseur.fetchone()
    res["station"] = result[0]
    res['Ligne'] = result[1]
    res["dest"] = result[2]
    res['time'] = convertor(result[4])
    return res
       



def next(station):
    res={}
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.execute("""SELECT route_short_name, stop_name, trip_headsign, timeline FROM infoarret WHERE Stop_name=?""",(station.upper(),))
    result = c.fetchall()
    
    for row in result:
        res["station"] = row[0]
        res['Ligne'] = row[1]
        res["dest"] = row[2]
        res['time'] = row[3]
        
    
    


   
    



# if __name__ == "__main__":
#     sys.exit(main()