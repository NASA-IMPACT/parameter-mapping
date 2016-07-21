# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-13 11:10:36
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-21 10:22:27

""" nc file dump and extract variables """
""" Library file for handling the uploaded hdf file
"""

import os
from scipy.io import netcdf

UPLOAD_DIR = "./uploads"
file_path = "../test/air.sig995.2012.nc"

"Extracting starts here"

# open the nc file for reading
def check():
	f = netcdf.netcdf_file(file_path, 'r')

	print dir(f)
	print "desc:", f.description
	print "dime:", f.dimensions
	print "file:", f.filename
	print "hist:", f.history
	print "plat:", f.platform
	print "titl:", f.title
	print "vari:", f.variables['lat']
	# print "vari:", f.variables['lat']['long_name']
	print "vari:", f.variables['lat'].long_name
	print "vari:", f.variables['lat'].standard_name
	print "vers:", f.version_byte


def sanitize(name):
	return str(name).replace("/", "_").replace(".", "_").replace(":", "_")


"""
return: dict(variable, dict((units, unitx), (details, description)))
"""
def get_variables(file_path):
	all_vars = dict()
	try:
		f = SD.SD(file_path, SD.SDC.READ)
		ds = f.datasets()
		for ds_name in ds:
			#open dataset
			d = f.select(ds_name)
			units = None if d.attributes().get('units') == 'none' else d.attributes().get('units')
			details = "%s %s" %(" ".join(d.dimensions().keys()), str(d.attributes().get('long_name')))
			details = details.replace("\n", " ").replace("/", " ").replace(".", " ").replace(":", " ")
			all_vars[sanitize(ds_name)] = dict(units=units, details=details)
			d.endaccess()
		f.end()
		return all_vars
	except Exception, e:
		print e
		raise


def main():
	check()
	# print get_variables(file_path)

if __name__ == '__main__':
	main()
