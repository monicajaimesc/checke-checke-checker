#!/usr/bin/python3
import requests as r
import time
from getpass import getpass
from sys import argv


def main():
    email = argv[1]
    pwd = getpass()
    api_key = input('enter api key: ')
    task = input('task number: ')
    data = {
            'api_key': api_key,
            'email': email,
            'password': pwd,
            'scope': 'checker'
            }
    s = r.Session()
    res = s.post('https://intranet.hbtn.io/users/auth_token.json', data=data)
    token = res.json().get('auth_token')
    # Get profile
    profile = s.get('https://intranet.hbtn.io/users/me.json?auth_token=' + str(token))
    # Get a project
    project = s.get('https://intranet.hbtn.io/projects/' + argv[2] + '.json?auth_token=' + str(token))
    # Get a task
    check = s.post('https://intranet.hbtn.io/tasks/' + task + '/start_correction.json?auth_token=' + str(token))
    #print(check.json())
    
    time.sleep(50)
    
    result = s.get('https://intranet.hbtn.io/correction_requests/' + str(check.json().get('id')) + '.json?auth_token=' + str(token))
    #for task in project.json().get('tasks'):
    #    print(task.get('title'))
    #    print(task.get('id'))
    print (result.json())    
    # task = s.get('https://intranet.hbtn.io/tasks/1007.json?auth_token=' )
    #print(project.json())

if __name__ == '__main__':
    main()
