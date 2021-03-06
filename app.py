from flask import Flask, render_template, jsonify
import fonctions as fc
from flask_cors import CORS
import back
import json
app = Flask(__name__)
CORS(app)
# CORS (Access-Control-Allow-Origin)

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

# @app.route('/Next/<station>')
# def station(station):
#     return jsonify(fc.next(station))


@app.route('/prochain')
def Next_tram():
    return jsonify(fc.next_tram())


if __name__=="__main__":
    app.run(debug=True)