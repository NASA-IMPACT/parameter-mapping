#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-11-25 10:53:58
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-21 12:06:32

from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
import os
import json
import time

from lib import libmapper, airs

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'hdf'])
UPLOAD_DIR = "uploads"

keywords = airs.AIRS_KEYWORDS
variables = airs.AIRS_VARIABLES
lookup = airs.Lookup(airs.AIRS_MAP)

final_map = None
uploaded_result = None


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def delete_previous_uploads():
    del_dir = os.path.join(basedir, UPLOAD_DIR)
    for path in os.listdir(del_dir):
        file_path = os.path.join(del_dir, path)
        try:
            os.remove(file_path)
        except:
            print "Cannot remove file: ", file_path

def upload_file(request):
    if request.method == 'POST':
        files = request.files.getlist('file')
        for f in files:
            if f and allowed_file(f.filename):
                delete_previous_uploads()   # delete other files from uploads
                filename = secure_filename(f.filename)
                updir = os.path.join(basedir, UPLOAD_DIR)
                f.save(os.path.join(updir, filename))
                file_size = os.path.getsize(os.path.join(updir, filename))
            else:
                app.logger.info('ext name error')
                return {"error": 'ext name errorr'}
                return jsonify(error='ext name error')
        return {"name": filename, "size": file_size}
        return jsonify(name=filename, size=file_size)


@app.route('/_show_it')
def add_numbers():
    korv = request.args.get('korv', 'ritesh', type=str)
    is_keyword = request.args.get('is_keyword', 1, type=int)
    print "KorV clicked in the list is : ", is_keyword, korv
    mapped = lookup.get_value(korv) if is_keyword else lookup.get_key(korv)
    return jsonify(result=mapped)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {"narr": 4}
    # variables = ["these", "are", "dynamic", "variables", "for", "testing"]
    # keywords = ["these", "are", "dynamic", "keywords", "for", "testing"]
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
    global final_map, uploaded_result
    errors = []
    results = {}
    # variables = ["these", "are", "dynamic", "variables", "for", "testing"]
    # keywords = ["these", "are", "dynamic", "keywords", "for", "testing"]
    uploaded_result = upload_file(request)
    # print uploaded_result.get_data(as_text=True)
    print uploaded_result.get('name', 'ritesh')
    return render_template('index.html', errors=errors, results=results, variables=variables, keywords=keywords)

@app.route('/mapping', methods=['GET', 'POST'])
def mapping():
    print uploaded_result
    if request.method == "POST":
        print "This is POST request"
    if request.method == "GET":
        print "This is GET request"
        # Read the hdf file and start extracting variables
        final_map = libmapper.start_mapping(uploaded_result, url=False)
        print "Final map is : ", final_map




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)