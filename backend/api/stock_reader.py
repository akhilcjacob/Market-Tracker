
import urllib, json
from flask import jsonify

def get_most_active():
    url = 'https://api.iextrading.com/1.0/stock/market/list/mostactive'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(data[1])
    return jsonify(data)
