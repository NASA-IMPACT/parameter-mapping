#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-16 10:42:47
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-06 11:04:51

import json
# from pymongo import MongoClient

import xml.etree.ElementTree as ET
tree = ET.parse("./xiang-docs/datasets.echo10.xml")



# def get_db():
# 	client = MongoClient('localhost', 27017)
# 	db = client.mapper
# 	return db

def sanitize(name):
	return name.replace("/", "_").replace(".", "_")


def main():
	root = tree.getroot()
	print root.tag
	print root.attrib
	print type(root)
	i = 0
	# db = get_db()
	for collection in root.iter('Collection'):
		short_name = collection.find('ShortName').text
		version = collection.find('VersionId').text
		long_name = collection.find('LongName').text
		dataset_id = collection.find('DataSetId').text
		science_keywords = collection.find('ScienceKeywords')
		daac_element = collection.find('ArchiveCenter')
		daac = daac_element.text if daac_element is not None else "None"

		f = open("science_keywords.txt", "a")

		name_keywords_dict = dict()
		name_keywords_dict["short_name"] = short_name
		name_keywords_dict["version"] = version
		name_keywords_dict["long_name"] = long_name
		name_keywords_dict["dataset_id"] = dataset_id
		name_keywords_dict["unique_name"] = sanitize(dataset_id)
		name_keywords_dict["daac"] = daac

		keyword_list = list()
		if science_keywords is not None:
			for keyword in science_keywords.iter('ScienceKeyword'):
				category = keyword.find('CategoryKeyword').text
				topic = keyword.find('TopicKeyword').text
				term = keyword.find('TermKeyword').text
				variables = keyword.findall(".//Value")
				for variable in variables:
					keyword_list.append("%s->%s->%s" %(topic.replace(" ", "_"), term.replace(" ", "_"), variable.text.replace(" ", "_")))
					# print category, topic, term, variable.text
			name_keywords_dict["keyword_list"] = keyword_list
			# print name_keywords_dict
			f.write(json.dumps(name_keywords_dict) + "\n")
			# db.keywords.insert_one(name_keywords_dict)
		f.close()
		# print name
		# if i >= 1:
		# 	break
		# i += 1
		# print i
	print "Keyword generation completed."


if __name__ == '__main__':
	main()

