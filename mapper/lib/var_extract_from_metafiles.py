# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-06-06 11:21:30
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-06-09 12:02:15


"""
1. dsu_generator
2. vs_generator
	- standard_name : cf-> gcmd
	- units: units -> cf -> gcmd
	- all available inputs
3. ms_generator

"""

import json
import glob
import requests


cf_units_file = "../../cf_units.json"
cf_gcmd_file = "../../cf_gcmd_map.json"

cf_units_base = "http://52.91.81.77:5003/service?units=%s"
cf_gcmd_base = "http://52.91.81.77:5001/service?cf=%s"

all_metadata_files = "../../all_metadata_files"
outfile = "../../variables.json"


def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def get_dataset_id_from_filename(filename):
	return filename.split("/")[-1]

def get_gcmd_keyword(cf):
	response = requests.get(cf_gcmd_base %(cf))
	data = json.loads(response.text)
	if not data:
		return None
	else:
		var = ""
		for gcmd in data:
			var = var + " " + gcmd.replace(">", "")
		return var.strip()


def get_gcmd_keyword_from_units(units):
	response = requests.get(cf_units_base %(units))
	data = json.loads(response.text)
	if not data:
		return None
	else:
		var = ""
		for cf_item in data:
			gcmds = get_gcmd_keyword(cf_item["cf"])
			if gcmds is not None:
				var = var + " " + gcmds
		return var.strip()

def main():
	count  = 0
	variable_detail_list = []
	for file in glob.glob("%s/*" %(all_metadata_files)):
		# print file
		dataset_id = get_dataset_id_from_filename(file)[:-len(".metadata.txt")]
		unique_name = sanitize(dataset_id)
		variable_dict = dict()
		ways = dict()
		print ". ", count; count += 1
		with open(file) as file_read:
			metadata = file_read.read()
			meta_var_list = metadata.split("variable")
			del meta_var_list[0]
			# print len(meta_var_list), meta_var_list
			for meta_var in meta_var_list:
				variable_name = meta_var[4:meta_var.find("\n")].strip()


				standard_start_idx = meta_var.find("standard_name")
				if standard_start_idx > 0:
					standard_end_idx = meta_var.find("\n", standard_start_idx)
					standard_name = meta_var[standard_start_idx+len("standard_name:=:"):standard_end_idx].strip()
					""" look up at cf->gcmd mappind """
					variable = get_gcmd_keyword(standard_name)
					if variable is not None and variable != "":
						variable_dict[variable_name] = variable
						ways[variable_name] = 1
						continue

				units_start_idx = meta_var.find("units")
				if units_start_idx > 0:
					units_end_idx = meta_var.find("\n", units_start_idx)
					units = meta_var[units_start_idx+len("units:=:"):units_end_idx].strip()
					""" look up at cf->gcmd mappind """
					variable = get_gcmd_keyword_from_units(units)
					if variable is not None and variable != "":
						variable_dict[variable_name] = variable
						ways[variable_name] = 2
						# variable_list.append(variable)
						# print "units"
						continue

				#take all as var
				# meta_var = unicode(meta_var, 'utf-8')
				variable = meta_var.decode("utf-8", "ignore").replace(":=:", " ").replace(":", " ").replace("/", " ").replace("\n", "").replace("\r", " ").strip()
				variable_dict[variable_name] = variable
				# variable_list.append(variable)
				# print "all"

		each_var_dict = {
			"meta_filename" : dataset_id,
			"unique_name" : unique_name,
			"variable_list": variable_dict,
			"ways": ways
		}
		variable_detail_list.append(each_var_dict)
		# if count >= 4:
		# 	break

	with open(outfile, "w") as variable_write:
		json.dump(variable_detail_list, variable_write, indent=4)

	print "\nJob Completed.\n"

if __name__ == '__main__':
	main()
