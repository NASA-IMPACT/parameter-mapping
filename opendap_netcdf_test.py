#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-11-20 11:24:31
# @Last Modified by:   ritesh
# @Last Modified time: 2015-11-25 11:15:42

import netCDF4

def main():
	url = r"http://hydro1.sci.gsfc.nasa.gov/dods/GLDAS_NOAH025SUBP_3H"
	dataset = netCDF4.Dataset(url)

	print dataset.title

	variables = dataset.variables
	variable_list = [key for key in variables.keys()]
	print "variables: ", variables.keys()
	vt = variables["time"]
	print vt[:]
	print vt.shape
	print type(vt)

	print dir(dataset)




if __name__ == '__main__':
	main()