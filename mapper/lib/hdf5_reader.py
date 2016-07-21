# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-13 11:41:39
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-21 16:24:12

""" Library file for handling the uploaded hdf file
"""
import os
import h5py

UPLOAD_DIR = "./uploads"
file_path = "../../DarkData/DataTypes/hdf5_type/1A.GPM.GMI.COUNT2016.20140304-S175932-E193159.000079.V04A.HDF5"

"Extracting starts here"

# open the hdf file for reading

def check():
	pass
	# def printname(name):
	# 	print name

	# f = h5py.File(file_path, 'r')

	# print "keys: ", f.keys()
	# print "vals: ", f.values()
	# print "attr: ", f.attrs
	# print "item: ", f.items
	# print "name: ", f.name

	# f.visit(printname)

	# first = f['gmi1aHeader/sampleRangeFile']
	# print "first: ", first
	# print "valu: ", first.attrs.items()

	# second = f['S1/sunData/phaseOfEclipseExit']
	# print "seco: ", second
	# print "valu: ", second.attrs.items()


	# grp = f['S1/scanStatus']
	# print "grp: ", grp
	# print "valu: ", grp.attrs.items()


	# grpp = f['S4/ScanTime']
	# print "grpp: ", grpp
	# print "valu: ", grpp.attrs.items()

	# for k,v in f.iteritems():
	# 	print k, len(v)
	# 	for kk, vv in v.iteritems():
	# 		print kk, len(vv)
	# 		break

	# for item in f.attrs.keys():
	#     print "***" , item + ":", f.attrs[item]


def sanitize(name):
	return str(name).replace("/", "_").replace(".", "_")

"""
@return: dict(variable, dict((units, unitx), (details, description)))
"""
def get_variables(file_path):
	all_vars = dict()
	try:
		f = h5py.File(file_path, 'r')

		var_list = list()
		def append_vars(name):
			if name not in var_list:
				var_list.append(name)
		f.visit(append_vars)

		for var in var_list:
			var_items = f[var].attrs.items()
			var_items_dict = dict(var_items)
			standard_name = var_items_dict.get("standard_name", None)
			units = var_items_dict.get("units", None)
			details = "%s %s" %(' '.join( ["%s %s" %(k, v) for k,v in var_items_dict.iteritems()]), var)
			details = details.replace("\n", " ").replace("/", " ").replace(".", " ")
			all_vars[sanitize(var)] = dict(standard_name=standard_name, units=units, details=details)

		return all_vars
	except Exception, e:
		print e
		# raise
		return


def main():
	print get_variables(file_path)

if __name__ == '__main__':
	main()




