from flask import Flask, render_template
import fonctions
import back
import json
app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello World'

@app.route('/All_lines')
def toutes_lignes(c):
    return jsonify(all_lines(c))

@app.route('/Next')
def Next(station):
    result = next_trip(station)


@app.route('/Next_tram')
def Next_tram(ligne, station, direction):
    result = next_tram(ligne, station, direction)


if __name__=="__main__":
    app.run(debug=True)