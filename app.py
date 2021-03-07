from flask import Flask, render_template, jsonify
import fonctions as f
import back
import json
app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
    entre = input("1 : All_lines, 2 : Next, 3 : Prochain")
    return entre

@app.route('/All_lines')
def toutes_lignes():
    return jsonify(f.all_lines())

@app.route('/Next/<station>')
def station(station):
    return jsonify(f.next(station))


@app.route('/prochain/<line>/<station>/<destination>')
def Next_tram(line, station, destination):
    return jsonify(f.next_tram(line, station, destination))


if __name__=="__main__":
    app.run(debug=True)