from flask import Flask, render_template, jsonify
import fonctions as fc
import back
import json
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def entry_point():
    return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
    return "Hello world"

@app.route('/All_lines')
def toutes_lignes():
    return jsonify(fc.all_lines())

@app.route('/Nextt/<station>')
def station(station):
    return jsonify(fc.nextt(station))


@app.route('/prochain/<line>/<station>/<destination>')
def Next_tram(line, station, destination):
    return jsonify(fc.next_tram(line, station, destination))


if __name__=="__main__":
    app.run(debug=True)
