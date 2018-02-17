
import urllib, json
from flask import jsonify

def get_most_active():
    url = 'https://api.iextrading.com/1.0/tops/last'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return jsonify(data)

def get_symbol(symbol):
    url = 'https://api.iextrading.com/1.0/stock/'+symbol+'/quote'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return jsonify(data)
