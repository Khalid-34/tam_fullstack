from flask import Flask, render_template, jsonify
import fonctions as fc
from flask_cors import CORS
import back
import json
app = Flask(__name__)
CORS(app)

@app.route('/')
def entry_point():
    return render_template('tam.html')

@app.route('/hello_world')
def hello_world():
    return "Hello world"

@app.route('/All_lines')
def toutes_lignes():
    """This shows all the lines that we have for all directions
    Parameters
    -------------
    All_lines : 'string'
    Type 'All_lines' to see all transports lines 

    Returns
    -------------
    All the transport line that we have up to now : ' string'
    """
    return jsonify(fc.all_lines())

@app.route('/Next')
def station():
    """This shows next trip avalaible from a station
    Parameters
    -------------
    Next : 'string'
    station : 'string'
    Type 'Next' first then the station stop name where you at

    Returns
    -------------
    Next trips that we gonna have from the stop name mentionned : ' string'
    """
    return jsonify(fc.next())



@app.route('/prochain/<line>/<station>/<destination>')
def Next_tram(line, station, destination):
    """This shows next trip avalaible from a station
    Parameters
    -------------
    prochain : 'string'
    line : 'string'
    stop_name : 'string'
    direction : 'string'
    http://127.0.0.1:5000/prochain/1/COMEDIE/MOSSON
    Type 'prochain' first then the 'line number' mention the 'stop' where you at
    and your 'destination'

    Returns
    -------------
    Next trip that goes to the direction you mentioned from the stop you at : ' string'
    """
    return jsonify(fc.next_tram(line, station, destination))


if __name__=="__main__":
    app.run(debug=True)