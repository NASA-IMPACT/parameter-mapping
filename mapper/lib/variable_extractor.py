#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-01-13 10:56:42
# @Last Modified by:   ritesh
# @Last Modified time: 2016-01-14 14:44:05

import h5py
from pyhdf import SD

import libmongo


def hdf_read(file_path):
	"""open the hdf 4 file for reading"""
	hdf = SD.SD(file_path, SD.SDC.READ)
	variable_list = list(set(hdf.datasets().keys()))
	print variable_list
	return variable_list

def hdf5_read(file_path):
	"""open the hdf 5 file for reading"""
	file = h5py.File(file_path, 'r')   # 'r' means that hdf5 file is open in read-only mode
	variable_list = file.keys()
	print variable_list
	return variable_list


def get_extension(file_path):
	return file_path.rsplit(".", 1)[-1]

def insert_variables(variable_list):
	db = libmongo.get_db()
	collection_id = "MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km V005"
	doc = {"name": collection_id, "variable_list": variable_list}
	result = db.vs.insert_one(doc)
	if result:
		print "Successfully Inserted"

ext_func = {"hdf": hdf_read, "h5": hdf5_read}

def extract(file_path, url=False):
	print url
	if not url:
		print "processing the uploaded file result"
		ext = get_extension(file_path)
		print ext

		"Extracting starts here"
		variable_list = ext_func.get(ext, hdf5_read)(file_path)
		"insert to db"
		# insert_variables(variable_list)


		# f = h5py.File(file_path, 'r')
		# print f.keys()

		# dataset = netCDF4.Dataset(file_path, mode='r')
		# print dataset.title

		return {"result": "this lib mapper working"}
	else:
		print "Processing the url provided"
		url  = path
		print url

def main():
	# file_path = "/Users/ritesh/Programming-stuffs/ITSC-projects/darkdata/mapping-science-keyword/granules/MOD04_L2.A2015345.1630.051.NRT.hdf"
	file_path = "/Users/ritesh/Programming-stuffs/ITSC-projects/darkdata/mapping-science-keyword/granules/MOD07_L2.A2016014.0745.005.2016014134404.hdf"
	extract(file_path, url=False)

if __name__ == '__main__':
	main()
