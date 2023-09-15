from flask import Flask, jsonify, request
from flask_cors import CORS
from create_a_search import data

flightSearchForm = []

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/search',methods=['GET'])
def get_search():
    return data({
        'departure': request.args.get('from'),
        'destination': request.args.get('to'),
        'departureDate': request.args.get('date'),
    })


if __name__ == '__main__':
    app.run(debug=True)