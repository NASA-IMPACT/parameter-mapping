# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-14 11:49:01
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-14 12:06:40


import os
import json

import libmongo

db = libmongo.get_db()

def avks_insert():
	vks_list = db.ms.find({}, {"_id":0, "vk": 1})
	db.avks.create_index([("variable", 1)])
	for vks in vks_list:
		print ".",
		vk = vks["vk"]
		for v in vk:
			ks = dict(vk[v]["mapped"])
			if len(ks) != 0:
				doc = {"variable": v, "keys": ks}
				db.avks.insert_one(doc)

	print "\nInsert to avsk Completed."


def main():
	avks_insert()

if __name__ == '__main__':
	main()