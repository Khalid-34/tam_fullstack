import sqlite3
import os
import sys
from back import main
from time import * 



def convertor(horaire):
    strftime('%M min %S sec', gmtime(horaire))
    return strftime('%M min %S sec', gmtime(horaire))


def all_lines():
    
    res = ['LIGNES:',]
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.row_factory= sqlite3.Row
    c.execute("""SELECT DISTINCT LIGNE FROM infoarret""")
    for row in c.fetchall():
        res.append(row[0])
    return res
        
        


def next_tram(): 
    
    res = {}
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.execute(" SELECT * FROM infoarret WHERE LIGNE = ? AND ARRET = ? AND DESTINATION = ? ")
    result = c.fetchone()
    res['LIGNE'] = result[0]
    res['ARRET'] = result[1]
    res['DESTINATION'] = result[3]
    res['ATTENTE'] = convertor(result[4])
    return res   

def next():
    res=[]
    conn=sqlite3.connect('trans_port.db')
    c = conn.cursor()
    c.row_factory= sqlite3.Row
    c.execute("SELECT LIGNE, ARRET, HORAIRE, DESTINATION FROM infoarret")
    result = c.fetchall()
    for row in result:
        res.append(dict(row))
    return res
    
# def next(station):
#     res=[]
#     conn=sqlite3.connect('trans_port.db')
#     c = conn.cursor()
#     c.row_factory= sqlite3.Row
#     c.execute("""SELECT LIGNE, ARRET, HORAIRE, DESTINATION FROM infoarret WHERE ARRET=?""",(station.upper(),))
#     result = c.fetchall()
#     for row in result:
#         res.append(dict(row))
#     return res
    
        
    
    


   
    



# if __name__ == "__main__":
#     sys.exit(main()