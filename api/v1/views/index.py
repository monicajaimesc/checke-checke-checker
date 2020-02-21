#!/usr/bin/python3
"""
this file has the end point route
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
import requests
import time

@app_views.route('/status', methods=["GET"])
def json_status():
    """
    return a json file
    """
    
    return jsonify({"status": "OK"})


@app_views.route('/auth', methods=["POST"], strict_slashes=False)
def authentification():
    """
    will request the auth_token
    """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if data.get('code_id') is None:
        abort(400, 'Missing code id')
    if data.get('password') is None:
        abort(400, 'Missing password')
    if data.get('api_key') is None:
        abort(400, 'Missing API_KEY')
    data = {
            'api_key': data.get('api_key'),
            'email': str(data.get('code_id')) + '@holbertonschool.com',
            'password': data.get('password'),
            'scope': 'checker' 
    }
    
    res = requests.post('https://intranet.hbtn.io/users/auth_token.json', data=data)
    token = res.json().get('auth_token')
        
    return jsonify(res.json())
    

@app_views.route('/project', methods=["POST"], strict_slashes=False)
def project():
    """
    return a dictionary that containt the project
    """
    # id project
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if data.get('project_id') is None:
        abort(400, 'Missing data')
    if data.get('auth_token') is None:
        abort(400, 'Missing token')
#
    project = requests.get('https://intranet.hbtn.io/projects/' + data.get('project_id') + '.json?auth_token=' + data.get('auth_token'))
    #  
    return jsonify(project.json())
    
    
@app_views.route('/task', methods=["POST"], strict_slashes=False)
def task():
    """
    """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if data.get('task_id') is None:
        abort(400, 'Missing task')
    if data.get('auth_token') is None:
        abort(400, 'Missing token')
#
    check = requests.post('https://intranet.hbtn.io/tasks/' + data.get('task_id') + '/start_correction.json?auth_token=' + str(data.get('auth_token')))

    time.sleep(120)
    
    result = requests.get('https://intranet.hbtn.io/correction_requests/' + str(check.json().get('id')) + '.json?auth_token=' + str(data.get('auth_token')))

    return jsonify(result.json())

        
    
    