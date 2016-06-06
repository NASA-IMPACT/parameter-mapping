# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-06-02 15:57:45
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-06-06 11:03:14

"""
1. dsu_generator
2. vs_generator
	- standard_name : cf-> gcmd
	- units: units -> cf -> gcmd
	- all available inputs
3. ms_generator

"""

import json

meta_formats = ["nc", "h5", "HDF5", "nc4", "he5", "hdf", "he5"]


infile = "../../datasets_to_url.txt"
outfile = "../../datasets_to_url.json"


def create_json():
	dsu_json = list()
	with open(infile) as dsu_read_txt:
		for line in dsu_read_txt:
			dataset_id, short_name, url = line.split("$")


			each_json = {
				"dataset_id" : dataset_id,
				"short_name" : short_name,
				"url" : url.strip()
				}

			dsu_json.append(each_json)

	with open(outfile, "w") as dsu_write_json:
		json.dump(dsu_json, dsu_write_json, indent=4)


def main():
	create_json()


if __name__ == '__main__':
	main()