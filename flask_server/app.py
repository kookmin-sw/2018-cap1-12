#!/usr/bin/python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/list')
def list():
	return render_template('list.html')

@app.route('/use')
def use():
	return render_template('use.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)