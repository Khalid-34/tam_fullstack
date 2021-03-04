from flask import Flask, render_template, jsonify
from fonctions import next

app = Flask(__name__)

@app.route('/')
def entry_point():
    return render_template('./app.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello World'


@app.route('/<station>')
def station(station):
    return jsonify(next(station))

if __name__ == '__main__':
    app.run(debug=True)