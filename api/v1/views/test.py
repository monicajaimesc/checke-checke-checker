#!/usr/bin/python3
import requests
import json

data = {
        'api_key': '6270b10d793dec57b222edd328ecfeaf',
        'code_id': '880',
        'password': 'Megustaelvino5',
        'scope': 'checker' 
}
authen = requests.post('http://0.0.0.0:5000/api/v1/auth', data=json.dumps(data), headers={'content-type':'application/json'})
print(authen.json())
auth_token = authen.json().get('auth_token')
data = {
    'task_id': '1712',
    'auth_token': auth_token
}
project = requests.post('http://0.0.0.0:5000/api/v1/task', data=json.dumps(data), headers={'content-type':'application/json'})
print(project.json())


