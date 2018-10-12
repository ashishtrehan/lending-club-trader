import json
from flask import Flask, request, abort, jsonify, Response



app = Flask(__name__)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
BASE_PATH = '/tsp/'

@app.route(BASE_PATH)
def home():
    return 'Lending Club Trader'

@app.route(BASE_PATH + 'index', methods=['GET'])
def index():
    app.logger.info("Inside pages url ")
    return Response(json.dumps({"status":"Success"}), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)