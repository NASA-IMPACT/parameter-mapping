# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-20 12:05:45
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-21 16:25:27

""" Library file for handling the uploaded hdf file
"""
import os
import netCDF4 		#netcdf-3




UPLOAD_DIR = "./uploads"
file_path = "../../DarkData/DataTypes/nc_type/20130425120000-UKMO-L4_GHRSST-SSTfnd-OSTIA-GLOB-v02.0-fv02.0.nc"

# UPLOAD_DIR = "./uploads"
# file_path = "../test/air.sig995.2012.nc"

"Extracting starts here"

# open the nc file for reading
def check():
	f = netCDF4.Dataset(file_path, mode='r')
	print f.title
	var = f.variables.get('lat')
	print var.long_name
	print f.file_format
	nc_attrs = f.ncattrs()
	print nc_attrs
	print repr(f.getncattr('description'))
	print var.ncattrs()
	print "Not" if 'undits' in var.ncattrs() else "not"



def sanitize(name):
	return str(name).replace("/", "_").replace(".", "_").replace(":", "_")

"""
return: dict(variable, dict((units, unitx), (details, description)))
"""
def get_variables(file_path):
	all_vars = dict()
	try:
		f = netCDF4.Dataset(file_path, mode='r')
		for var in f.variables:
			if var != 'None':
				attrs = f.variables.get(var).ncattrs()
				units = f.variables.get(var).getncattr('units') if 'units' in attrs else None
				standard_name = f.variables.get(var).getncattr('standard_name') if 'standard_name' in attrs else None
				long_name = f.variables.get(var).getncattr('long_name') if 'long_name' in attrs else None
				details = f.variables.get(var).getncattr('description') if 'description' in attrs else None
				var_name = var
				if standard_name is not None:
					var_name = standard_name
				if var_name or long_name or details:
					details = "%s %s %s" %(long_name, details, var_name)
				all_vars[sanitize(var_name)] = dict(standard_name=standard_name, units=units, details=str(details))
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

