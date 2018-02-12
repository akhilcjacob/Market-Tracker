from random import *
from flask_cors import CORS
from flask import Flask, render_template, jsonify

import sys
sys.path.insert(0, 'api/')
from stock_reader import *

app = Flask(__name__,   static_folder = "../dist/static",
                        template_folder = "../dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/stocks')
def getMostUsed():
    # response = {
        # 'stock': get_most_active()
    # }
    # return jsonify(response)
    return get_most_active()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def defaults(path):
    return render_template("index.html")

