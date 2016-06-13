# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-06-06 16:01:06
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-06-09 21:16:28

""" Mongodb
    Database    :       mapper
    Collections :
            keywords    :   ks
            variables   :   vs
            maps        :   ms
            data_url	:	dsu
"""

import libmongo
import json

dsu_file = "../../datasets_to_url.json"
vs_file = "../../variables_with_dataset_id.json"
ks_file = "../../science_keywords.txt"

db = libmongo.get_db()

def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def dsu_insert():
	# db.dsu.create_index(["unique_name"])
	with open(dsu_file) as dsu_readfile:
		data = json.load(dsu_readfile)
		db.dsu.insert(data)
	print "dsu insert completed..."

def vs_insert():
	with open(vs_file) as vs_readfile:
		data = json.load(vs_readfile)
		db.vs.insert(data)
	db.vs.create_index([("unique_name", 1)])
	print "vs insert completed..."

def ks_insert():
	with open(ks_file) as ks_readfile:
		data = json.load(ks_readfile)
		db.ks.insert(data)
	db.ks.create_index([("unique_name", 1)])
	print "ks insert completed..."

def main():
	# dsu_insert()
	vs_insert()
	# ks_insert()
	print "Job Completed. \n"

if __name__ == '__main__':
	main()

