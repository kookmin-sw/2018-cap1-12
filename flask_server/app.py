#!/usr/bin/python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for, send_from_directory
from werkzeug import secure_filename
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'static/pictures/'			#업로드된 파일이 저장되는 곳
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])	#허용할 파일 확장자

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

font_dir = "static/fonts"
tt = os.walk(font_dir).next()[2]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/list')
def list():
	return render_template('list.html', tt=tt)

@app.route('/use')
def use():
	return render_template('use.html')

@app.route('/text/<fontname>')
def text(fontname):
	return render_template('text.html', fontname = fontname)

@app.route('/uploadFile/<filename>')
def uploadFile(filename):
	return render_template('uploadFile.html', filename=filename)

@app.route('/display')
def display_cutImage():
	return render_template('cutImage.html')

@app.route('/uploadFile/cutImage', methods=['GET', 'POST'])
def cutImage():
	if request.method == 'POST':
		filename = request.form['filename']
		lineNumber = request.form['lineNumber']
		ttfName = request.form['ttfName']
		print lineNumber
		print ttfName
		print filename
		return redirect(url_for('display_cutImage'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	uploaded_files = request.files.getlist('profile[]')
	filenames = []
	if request.method == 'POST':
		for file in uploaded_files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)	#파일명 보호
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				filenames.append(filename)
		return redirect(url_for("uploadFile", filename=filename))

@app.route('/header')
def header():
	return render_template('header.html')

@app.route('/head')
def head():
	return render_template('head.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)