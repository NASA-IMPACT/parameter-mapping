#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-10 11:14:18
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-14 17:31:11

""" Library file for handling the uploaded hdf file
	Also works with the url
"""

import os
import hdf5_reader

import libmongo
import re
import json

import var_extract_from_metafiles
from acronyms import ACRONYMS, DISCARDS

UPLOAD_DIR = "./uploads"
UPLOAD_JSON_DIR = "./uploads_json"

celery_current = 0
celery_total = 1

db = libmongo.get_db()

def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def get_filepath(upload_result):
	filename = upload_result["name"]
	file_path = os.path.join(os.path.abspath(UPLOAD_DIR), filename)
	return file_path

def get_json_filepath(upload_result):
	filename = upload_result["name"]
	json_filepath = os.path.join(os.path.abspath(UPLOAD_JSON_DIR), filename)
	return json_filepath

def get_celery_current():
	return celery_current

def get_celery_total():
	return celery_total

def get_map_from_uplaod(variables):
	global celery_current, celery_total
	variable_map = dict()
	cfk = dict()
	cfu = dict()
	cfdb = dict()
	celery_total = len(variables)

	for variable_name in variables:
		celery_current = celery_current + 1
		print celery_current
		skip = False
		for skip_var in DISCARDS:
			if skip_var in variable_name.lower():
				# print "found: %s as %s" %(skip_var, variable_name)
				skip = True
				break

		if not skip:
			var_standard_name = variables[variable_name].get("standard_name", None)
			if var_standard_name is not None and var_standard_name is not "":
				""" look up at cf->gcmd mapping """
				gcmd_list = list(set(var_extract_from_metafiles.get_gcmd_keyword_list(var_standard_name)))
				if gcmd_list is not None and len(gcmd_list) != 0:
					cfk[variable_name] = list(gcmd_list)
					continue

			var_units = variables[variable_name].get("units", None)
			if var_units is not None and var_units is not "":
				""" look up at units->cf->gcmd mapping """
				gcmd_list = list(set(var_extract_from_metafiles.get_gcmd_keyword_list_from_units(var_units)))
				if gcmd_list is not None and len(gcmd_list) != 0:
					variable_name_with_unit = "%s (%s)" %(variable_name, var_units)
					cfu[variable_name_with_unit] = list(gcmd_list)
					continue

			kfdb = db.avks.find({"variable": variable_name}, {"_id": 0, "keys": 1}).limit(1)
			cfdb[variable_name] = dict(dict(kfdb).get("keys", {}))

	variable_map['cfk'] = cfk
	variable_map['cfu'] = cfu
	variable_map['cfdb'] = cfdb

	return variable_map


def start_mapping(upload_result, url=False):
	print url

	if not url:
		print "processing the uploaded file result"
		file_path = get_filepath(upload_result)
		json_filepath = get_json_filepath(upload_result)
		# file_path = "../../DarkData/DataTypes/hdf5_type/1A.GPM.GMI.COUNT2016.20140304-S175932-E193159.000079.V04A.HDF5"
		"Extracting starts here"
		"""open the hdf file for reading"""
		#hdf5
		try:
			variables = hdf5_reader.get_variables(file_path)
			variable_map = get_map_from_uplaod(variables)
			with open(json_filepath, "w") as json_write:
				json.dump(variable_map, json_write, indent=4)
			return variable_map

		except Exception, e:
			print "Here is exception: (libmapper): ", e
			return
	else:
		print "Processing the url provided"
		url  = upload_result
		print url
		return {"Success": True}

def main():
	# file_path = "/Users/ritesh/Programming-stuffs/ITSC-projects/darkdata/mapping-science-keyword/mapper/uploads/MOD04_L2.A2015345.1630.051.NRT.hdf"
	# file_path = "../../DarkData/DataTypes/hdf5_type/1A.GPM.GMI.COUNT2016.20140304-S175932-E193159.000079.V04A.HDF5"
	file_path = "1A.GPM.GMI.COUNT2016.20140304-S175932-E193159.000079.V04A.HDF5"

	upload_result = {"name": file_path}
	result = start_mapping(upload_result, url=False)
	print result

if __name__ == '__main__':
	main()
