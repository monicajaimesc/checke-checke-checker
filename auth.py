#!/usr/bin/python3
import requests as r
from getpass import getpass
from sys import argv

API_KEY = '3214b861a938a0fcf34d0bc835647d45'

def main():
    email = argv[1]
    pwd = getpass()
    data = {
            'api_key': API_KEY,
            'email': email,
            'password': pwd,
            'scope': 'checker'
            }
    s = r.Session()
    res = s.post('https://intranet.hbtn.io/users/auth_token.json', data=data)
    token = res.json().get('auth_token')
    profile = s.get('https://intranet.hbtn.io/users/me.json?auth_token=' + API_KEY)
    # Get a project
    # project = s.get('https://intranet.hbtn.io/projects/' + argv[2] + '.json?auth_token=' + API_KEY)
    print(profile.json())

if __name__ == '__main__':
    main()
