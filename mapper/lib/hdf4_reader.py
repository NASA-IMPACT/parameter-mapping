# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-13 15:18:04
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-21 16:18:13

""" Library file for handling the uploaded hdf file
"""
import os
from pyhdf import SD 		#hdf4

UPLOAD_DIR = "./uploads"
file_path = "../../DarkData/DataTypes/hdf_type/MYDATML2.A2002185.0000.051.2008315212231.hdf"

"Extracting starts here"

# open the hdf file for reading
def check():
	hdf4 = SD.SD(file_path, SD.SDC.READ)
	ds = hdf4.datasets()
	print ds
	cp = hdf4.select("Precipitable_Water_Near_Infrared_Clear")
	print " ".join(cp.dimensions().keys()),  cp.attributes(), cp.attributes().get('units')

	cp.endaccess()
	hdf4.end()


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
			details = "%s %s %s" %(" ".join(d.dimensions().keys()), str(d.attributes().get('long_name')), ds_name)
			details = details.replace("\n", " ").replace("/", " ").replace(".", " ").replace(":", " ")
			all_vars[sanitize(ds_name)] = dict(standard_name=ds_name, units=units, details=details)
			d.endaccess()
		f.end()
		return all_vars
	except Exception, e:
		print e
		# raise
		return


def main():
	# check()
	print get_variables(file_path)

if __name__ == '__main__':
	main()








