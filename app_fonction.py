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
    return jsonify(fc.all_lines())

@app.route('/Next')
def station():
    return jsonify(fc.next())


@app.route('/prochain/<line>/<station>/<destination>')
def Next_tram(line, station, destination):
    return jsonify(fc.next_tram(line, station, destination))


if __name__=="__main__":
    app.run(debug=True)