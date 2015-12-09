#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-11-25 10:53:58
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-09 12:50:24

from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

UPLOAD_DIR = "uploads"
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'hdfs'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def upload_file(request):
    if request.method == 'POST':
        files = request.files.getlist('file')
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                updir = os.path.join(basedir, UPLOAD_DIR)
                f.save(os.path.join(updir, filename))
                file_size = os.path.getsize(os.path.join(updir, filename))
            else:
                app.logger.info('ext name error')
                return jsonify(error='ext name error')
        return jsonify(name=filename, size=file_size)


@app.route('/_show_it')
def add_numbers():
    variable = request.args.get('variable', 'ritesh', type=str)
    print "Variable clicked in the list is : ", variable
    return jsonify(result=variable)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {"narr": "ritesh"}
    variables = ["these", "are", "dynamic", "variables", "for", "testing"]
    keywords = ["these", "are", "dynamic", "keywords", "for", "testing"]
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            # r = requests.get(url)
            r = url
            print r
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors, results=results, variables=variables, keywords=keywords)
        if r:
        	results[r] = len(r)
        	for result in results:
        		print result[0], result[1]
        	print results
	print results
	print variables
    return render_template('index.html', errors=errors, results=results, variables=variables, keywords=keywords)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    errors = []
    results = {}
    variables = ["these", "are", "dynamic", "variables", "for", "testing"]
    keywords = ["these", "are", "dynamic", "keywords", "for", "testing"]
    upload_result = upload_file(request)
    print upload_result.get_data(as_text=True)
    return render_template('index.html', errors=errors, results=results, variables=variables, keywords=keywords)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)