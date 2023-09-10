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

@app.route('/results',methods=['GET'])
def display_skyscanner_response():
    print(data(flightSearchForm))
    return data(flightSearchForm)

@app.route('/search',methods=['POST'])
def get_search():
    post_data = request.get_json()
    app.logger.debug("Received POST data: %s", post_data)
    flightSearchForm.append({
        'departure': post_data.get('departure'),
        'destination': post_data.get('destination'),
        'departureDate': post_data.get('departureDate'),
        'returnDate': post_data.get('returnDate')
    })
    app.logger.debug("flightSearchForm: %s", flightSearchForm) 

    return jsonify(flightSearchForm)


if __name__ == '__main__':
    app.run(debug=True)