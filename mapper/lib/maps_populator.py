#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-01-14 10:35:45
# @Last Modified by:   ritesh
# @Last Modified time: 2016-01-20 10:05:51

"""From the list of keyword in ks db collection
	and list of variable in vs db collection
	populate the maps in ms collection for corresponding echo collection name.
"""

import libmongo
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from textblob import TextBlob


db = libmongo.get_db()
word_tokenizer = RegexpTokenizer(r'\w+')
wordnet_lemmatizer = WordNetLemmatizer()

print "convert into lemmas (normal form)"
def split_into_lemmas(message):
    # message = unicode(message, 'utf-8').lower()
    # tokenized_words = word_tokenizer.tokenize(message)
	# words = TextBlob(message).words
    # # for each word, take its "base form" = lemma
    # return [word.lemma for word in words]
    message = message.lower()
    words = re.split(r"[>/_-]+", message)
    return [wordnet_lemmatizer.lemmatize(word) for word in words]

def sanitize(name):
	return name.replace("/", "_").replace(".", "_")

def diff(a, b):
	b = set(b)
	return [aa for aa in a if aa not in b]

def kv_generator(keywords, variables):
	kv = dict()
	for keyword in keywords:
		kvd = dict()
		mapped = dict()
		ranked = dict()
		keyword_parts = set(split_into_lemmas(keyword))
		for variable in variables:
			variable_parts = set(split_into_lemmas(variable))
			print keyword, keyword_parts, variable_parts
			rank = len(keyword_parts & variable_parts)
			if rank <= 0:
				ranked[variable.replace(".", "_")] = rank
			else:
				mapped[variable.replace(".", "_")] = rank
		kvd["mapped"] = mapped
		kvd["ranked"] = ranked
		kv[keyword.replace(".", "_")] = kvd
	return kv

def vk_generator(variables, keywords):
	print "In vk generator"
	vk = dict()
	for variable in variables:
		vkd = dict()
		mapped = dict()
		ranked = dict()
		variable_parts = set(split_into_lemmas(variable))
		for keyword in keywords:
			keyword_parts = set(split_into_lemmas(keyword))
			print variable, variable_parts, keyword_parts
			rank = len(keyword_parts & variable_parts)
			if rank <= 0:
				ranked[keyword.replace(".", "_")] = rank
			else:
				mapped[keyword.replace(".", "_")] = rank
		vkd["mapped"] = mapped
		vkd["ranked"] = ranked
		vk[variable.replace(".", "_")] = vkd
	return vk

# def kv_generator(keywords, variables):
# 	kv = dict()
# 	for keyword in keywords:
# 		kvl = list()
# 		keyword_parts = set(split_into_lemmas(keyword))
# 		for variable in variables:
# 			variable_parts = set(split_into_lemmas(variable))
# 			print keyword, keyword_parts, variable_parts
# 			rank = len(keyword_parts & variable_parts)
# 			if rank >= 1:
# 				kvl.append(variable)
# 		kv[keyword.replace(".", "_")] = kvl
# 	return kv

# def vk_generator(variables, keywords):
# 	print "In vk generator"
# 	vk = dict()
# 	for variable in variables:
# 		vkl = list()
# 		variable_parts = set(split_into_lemmas(variable))
# 		for keyword in keywords:
# 			keyword_parts = set(split_into_lemmas(keyword))
# 			print variable, variable_parts, keyword_parts
# 			rank = len(keyword_parts & variable_parts)
# 			if rank >= 1:
# 				vkl.append(keyword)
# 		vk[variable.replace(".", "_")] = vkl
# 	return vk


def doc_generator(variables, keywords):
	kv = kv_generator(keywords, variables)
	print "--- Printing kv generated ---"
	print kv

	vk = vk_generator(variables, keywords)
	print "--- Printing vk generated ---"
	print vk

	return kv, vk

def populate(to_map_colls):
	for coll in to_map_colls:
		print "Updating %s Collection" %(coll)
		variables = db.vs.find_one({"name": coll}, {"variable_list":1, "_id": 0})["variable_list"]
		keywords = db.ks.find_one({"dataset_id": coll}, {"keyword_list":1, "_id": 0})["keyword_list"]
		print variables
		print keywords
		kv, vk = doc_generator(variables, keywords)
		doc = {"name": coll, "kv": kv, "vk": vk}
		result = db.ms.insert_one(doc)
		if result:
			print "Successfully Inserted '%s' collection maps" %(coll)

def temp_sanitize_names():
	keywords_docs = db.ks.find()
	for keywords_doc in keywords_docs:
		db.ks.update({"dataset_id":keywords_doc["dataset_id"]}, {"$set": {"dataset_id": sanitize(keywords_doc["dataset_id"])}})
	print "Ks update complete"

	variables_docs = db.vs.find()
	for variables_doc in variables_docs:
		db.vs.update({"name":variables_doc["name"]}, {"$set": {"name": sanitize(variables_doc["name"])}})
	print "vs update complete"

	maps_docs = db.ms.find()
	for maps_doc in maps_docs:
		db.ms.update({"name":maps_doc["name"]}, {"$set": {"name": sanitize(maps_doc["name"])}})
	print "ms update complete"


def main():
	colls_in_ks = [k["dataset_id"] for k in db.ks.find({}, {"dataset_id":1, "_id": 0})]
	colls_in_vs = [v["name"] for v in db.vs.find({}, {"name":1, "_id": 0})]
	colls_in_ms = [m["name"] for m in db.ms.find({}, {"name":1, "_id": 0})]

	print colls_in_ks
	print colls_in_vs
	print colls_in_ms

	print "diff in coll_ks and coll_vs", diff(colls_in_ks, colls_in_vs)
	super_colls = colls_in_ks if len(set(colls_in_ks)) >= len(set(colls_in_vs)) else colls_in_vs
	to_map_colls = diff(super_colls, colls_in_ms)
	populate(to_map_colls)


if __name__ == '__main__':
	main()
	# temp_sanitize_names()


