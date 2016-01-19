#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-10 11:14:18
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-21 15:11:11

""" Library file for handling the uploaded hdf file
	Also works with the url
"""
import os
# import netCDF4
import h5py
from pyhdf import SD

UPLOAD_DIR = "./uploads"

def start_mapping(upload_result, url=False):
	print url
	if not url:
		print "processing the uploaded file result"
		filename = upload_result["name"]
		file_path = os.path.join(os.path.abspath(UPLOAD_DIR), filename)

		"Extracting starts here"
		# open the hdf file for reading
		hdf = SD.SD(file_path, SD.SDC.READ)
		print hdf.datasets()
		print dir(hdf)
		print hdf.info()
		print dir(hdf.attr())
		# f = h5py.File(file_path, 'r')
		# print f.keys()

		# dataset = netCDF4.Dataset(file_path, mode='r')
		# print dataset.title

		return {"result": "this lib mapper working"}
	else:
		print "Processing the url provided"
		url  = upload_result
		print url

def main():
	file_path = "/Users/ritesh/Programming-stuffs/ITSC-projects/darkdata/mapping-science-keyword/mapper/uploads/MOD04_L2.A2015345.1630.051.NRT.hdf"
	upload_result = {"name": file_path}
	start_mapping(upload_result, url=False)

if __name__ == '__main__':
	main()
