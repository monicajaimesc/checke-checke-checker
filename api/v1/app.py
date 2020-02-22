#!/usr/bin/python3
"""
This file will start an API
"""
from api.v1.views import app_views
from flask import jsonify, make_response
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

host="0.0.0.0"
port="5000"


CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

def send_json_error(err, code):
    """
    Sends an error using JSON
    """
    msg = str(err).split(': ')[1]
    context = {'error': msg}
    return make_response(jsonify(**context), code)


@app.errorhandler(400)
def bad_request(err):
    """
    Handles 400 error
    """
    return send_json_error(err, 400)


@app.errorhandler(404)
def not_found(err):
    """
    Handles 404 error
    """
    print(err)
    return send_json_error("error: Not found", 404)





if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
