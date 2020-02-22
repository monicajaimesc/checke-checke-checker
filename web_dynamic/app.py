#!/usr/bin/python3
"""
Flask App that integrates with Checker static HTML Template
"""
from flask import Flask, render_template, url_for


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5001
host = '0.0.0.0'



@app.route('/registration')
def register():
    return render_template('Registro.html')

@app.route('/project')
def project():
    return render_template('cheker1.html')

@app.route('/tasks')
def tasks():
    return render_template('cheker2.html')

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)