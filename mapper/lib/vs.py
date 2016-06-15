# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-06-07 11:45:55
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-06-14 14:28:12


dsu_file = "../../datasets_to_url.json"
variables_file = "../../variables.json"
outfile = "../../variables_with_dataset_id.json"

import json

def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def main():

	with open(dsu_file) as dsu_read:
		dsu_data = json.load(dsu_read)

	with open(variables_file) as variables_read:
		variables_data = json.load(variables_read)

	vs = []
	for v in variables_data:
		for dsu in dsu_data:
			if v["meta_filename"] in dsu["url"]:
				variable_list = dict((sanitize(key), value) for (key, value) in v["variable_list"].items())
				ways = dict((sanitize(key), value) for (key, value) in v["ways"].items())
				cfk = dict((sanitize(key), list(set(value))) for (key, value) in v["cfk"].items())
				cfu = dict((sanitize(key), list(set(value))) for (key, value) in v["cfu"].items())
				each_vs = {
					"dataset_id" : dsu["dataset_id"],
					"unique_name" : sanitize(dsu["dataset_id"]),
					"variable_list" : variable_list,
					"url": dsu["url"],
					"ways": ways,
					"cfk": cfk,
					"cfu": cfu

				}

				vs.append(each_vs)
				break

	with open(outfile, "w") as outfile_write:
		json.dump(vs, outfile_write, indent=4)

	print "\n Job Completed.\n"

if __name__ == '__main__':
	main()