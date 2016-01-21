#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-11-25 10:53:58
# @Last Modified by:   ritesh
# @Last Modified time: 2016-01-21 00:04:02

from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug import secure_filename
import os
import json
import time
import operator

from lib import libmapper, airs, libmongo

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'hdf'])
UPLOAD_DIR = "uploads"

keywords = airs.AIRS_KEYWORDS
variables = airs.AIRS_VARIABLES
lookup = airs.Lookup(airs.AIRS_MAP)

final_map = None
uploaded_result = None
collections = None

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

def get_sorted_kv_map(maps):
    kv_map = dict()
    for k, mrd in maps["kv"].iteritems():
        kv_map[k] = {
                    "mapped" : sorted(mrd["mapped"].items(), key=operator.itemgetter(1), reverse=True),
                    "ranked" : sorted(mrd["ranked"].items(), key=operator.itemgetter(1), reverse=True)
                    }
    return kv_map


def get_sorted_vk_map(maps):
    vk_map = dict()
    for k, mrd in maps["vk"].iteritems():
        vk_map[k] = {
                    "mapped" : sorted(mrd["mapped"].items(), key=operator.itemgetter(1), reverse=True),
                    "ranked" : sorted(mrd["ranked"].items(), key=operator.itemgetter(1), reverse=True)
                    }
    return vk_map




@app.route('/_show_it')
def add_numbers():
    korv = request.args.get('korv', 'ritesh', type=str)
    is_keyword = request.args.get('is_keyword', 1, type=int)
    print "KorV clicked in the list is : ", is_keyword, korv
    mapped = lookup.get_value(korv) if is_keyword else lookup.get_key(korv)
    return jsonify(result=mapped)

@app.route('/_show_map/<collection_name>', methods=['GET', 'POST'])
def show_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    # collection_name = request.args.get('collection_name', 'ritesh', type=str)
    print "Collection clicked in the list is : ", collection_name
    db = libmongo.get_db()
    keywords = db.ks.find_one({"dataset_id": collection_name}).get("keyword_list")
    variables = db.vs.find_one({"name": collection_name}).get("variable_list")
    maps = db.ms.find_one({"name": collection_name})
    print keywords, variables, maps

    return render_template('maps.html', errors=errors, results=results, variables=variables, keywords=keywords, maps=maps, collections=collections)


@app.route('/save_keyword_map/', methods=['POST'])
def save_keyword_map():
    data = request.data
    print "Obtained data from map form: ", data
    print request.args
    print request.form
    print request.values
    return redirect(url_for("index"))

@app.route('/_show_keyword_map/<collection_name>', methods=['GET', 'POST'])
def show_keyword_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    # collection_name = request.args.get('collection_name', 'ritesh', type=str)
    print "Collection clicked in the list iddds : ", collection_name
    db = libmongo.get_db()
    keywords = db.ks.find_one({"dataset_id": collection_name}).get("keyword_list")
    variables = db.vs.find_one({"name": collection_name}).get("variable_list")
    maps = db.ms.find_one({"name": collection_name})
    print keywords, variables, maps
    sorted_maps = dict()
    sorted_maps["name"] = collection_name
    sorted_maps["kv"] = get_sorted_kv_map(maps)
    sorted_maps["vk"] = get_sorted_vk_map(maps)

    print sorted_maps

    return render_template('show_keyword_map.html', errors=errors, results=results, variables=variables, \
        keywords=keywords, maps=maps, collections=collections, \
        sorted_maps=sorted_maps)


@app.route('/_edit_keyword_map/<collection_name>', methods=['GET', 'POST'])
def edit_keyword_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    # collection_name = request.args.get('collection_name', 'ritesh', type=str)
    print "Collection clicked in the list iddds : ", collection_name
    db = libmongo.get_db()
    keywords = db.ks.find_one({"dataset_id": collection_name}).get("keyword_list")
    variables = db.vs.find_one({"name": collection_name}).get("variable_list")
    maps = db.ms.find_one({"name": collection_name})
    print keywords, variables, maps

    sorted_maps = dict()
    sorted_maps["name"] = collection_name
    sorted_maps["kv"] = get_sorted_kv_map(maps)
    sorted_maps["vk"] = get_sorted_vk_map(maps)

    return render_template('edit_keyword_map.html', errors=errors, results=results, variables=variables, \
        keywords=keywords, maps=maps, collections=collections, \
        sorted_maps=sorted_maps)


@app.route('/_edit_variable_map/<collection_name>', methods=['GET', 'POST'])
def edit_variable_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    # collection_name = request.args.get('collection_name', 'ritesh', type=str)
    print "Collection clicked in the list iddds : ", collection_name
    db = libmongo.get_db()
    keywords = db.ks.find_one({"dataset_id": collection_name}).get("keyword_list")
    variables = db.vs.find_one({"name": collection_name}).get("variable_list")
    maps = db.ms.find_one({"name": collection_name})
    print keywords, variables, maps

    sorted_maps = dict()
    sorted_maps["name"] = collection_name
    sorted_maps["kv"] = get_sorted_kv_map(maps)
    sorted_maps["vk"] = get_sorted_vk_map(maps)

    return render_template('edit_variable_map.html', errors=errors, results=results, variables=variables, \
        keywords=keywords, maps=maps, collections=collections, \
        sorted_maps=sorted_maps)


@app.route('/_update_keyword_map/<collection_name>', methods=['GET', 'POST'])
def update_keyword_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    TO_UPDATE = {}
    if request.method == 'POST':
        print "here is the update thing "
        print list(request.form.keys())
        db = libmongo.get_db()
        col_map = db.ms.find_one({"name": collection_name})
        print col_map
        for keyword in request.form.keys():
            variables = request.form.getlist(keyword)
            variables = list(set(variables))
            key = keyword.split("-", 2)[-1]
            old_mapped_kv = col_map.get("kv").get(key).get("mapped")
            old_ranked_kv = col_map.get("kv").get(key).get("ranked")
            old_mapped_kv_set = set(old_mapped_kv.keys())
            old_ranked_kv_set = set(old_ranked_kv.keys())
            new_mapped_kv_set = set()
            mapped_d = dict()
            ranked_d = dict()
            for variable in variables:
                v, i = variable.split("-->",1)
                mapped_d[v] = int(i)         #populate mapped new
                new_mapped_kv_set.add(v)

            added_to_mapped = new_mapped_kv_set.difference(old_mapped_kv_set)
            removed_from_mapped = old_mapped_kv_set.difference(new_mapped_kv_set)

            for am_key in added_to_mapped:
                del old_ranked_kv[am_key]       #remove from ranked
            for ar_key in removed_from_mapped:
                old_ranked_kv[ar_key] = old_mapped_kv[ar_key]   #populate ranked map / add to ranked

            TO_UPDATE[key] = {"mapped" : mapped_d, "ranked": old_ranked_kv}
        print "things to update is :", TO_UPDATE

    print "Collection clicked in the list iddds : ", collection_name

    query = {"name": collection_name}
    update = {"$set": {"kv": TO_UPDATE}}
    result = db.ms.update_one(query, update)
    if result.matched_count == 1:
        print "Successful update"
    # keywords = db.ks.find_one({"dataset_id": collection_name}).get("keyword_list")
    # variables = db.vs.find_one({"name": collection_name}).get("variable_list")
    # maps = db.ms.find_one({"name": collection_name})
    # print keywords, variables, maps
    return redirect(url_for("show_keyword_map", collection_name=collection_name))
    # return render_template('edit_keyword_map.html', errors=errors, results=results, variables=variables, keywords=keywords, maps=maps, collections=collections)

@app.route('/_update_variable_map/<collection_name>', methods=['GET', 'POST'])
def update_variable_map(collection_name):
    errors = []
    results = {"four": 4}
    print collection_name
    TO_UPDATE = {}
    if request.method == 'POST':
        print "here is the update thing  for variable"
        db = libmongo.get_db()
        col_map = db.ms.find_one({"name": collection_name})
        for variable in request.form.keys():
            keywords = request.form.getlist(variable)
            keywords = list(set(keywords))
            key = variable.split("-", 2)[-1]

            old_mapped_vk = col_map.get("vk").get(key).get("mapped")
            old_ranked_vk = col_map.get("vk").get(key).get("ranked")
            old_mapped_vk_set = set(old_mapped_vk.keys())
            old_ranked_vk_set = set(old_ranked_vk.keys())
            new_mapped_vk_set = set()

            mapped_d = dict()
            ranked_d = dict()
            for keyword in keywords:
                v, i = keyword.split("-->",1)
                mapped_d[v] = int(i)         #populate mapped new
                new_mapped_vk_set.add(v)

            added_to_mapped = new_mapped_vk_set.difference(old_mapped_vk_set)
            removed_from_mapped = old_mapped_vk_set.difference(new_mapped_vk_set)

            for am_key in added_to_mapped:
                del old_ranked_vk[am_key]       #remove from ranked
            for ar_key in removed_from_mapped:
                old_ranked_vk[ar_key] = old_mapped_vk[ar_key]   #populate ranked map / add to ranked

            TO_UPDATE[key] = {"mapped" : mapped_d, "ranked": old_ranked_kv}

        print "things to update is :", TO_UPDATE

    print "Collection clicked in the list iddds : ", collection_name

    query = {"name": collection_name}
    update = {"$set": {"vk": TO_UPDATE}}
    result = db.ms.update_one(query, update)
    if result.matched_count == 1:
        print "Successful  variable map update"
    return redirect(url_for("show_keyword_map", collection_name=collection_name))
    # return render_template('edit_keyword_map.html', errors=errors, results=results, variables=variables, keywords=keywords, maps=maps, collections=collections)


@app.route('/', methods=['GET', 'POST'])
def index():
    global collections
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
    try:
        db = libmongo.get_db()
        collections = db.ms.find()
    except Exception, e:
        print "Db exception error"
    return render_template('index.html', errors=errors, results=results, variables=variables, keywords=keywords, collections=collections)


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