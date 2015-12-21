#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-11-20 11:24:31
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-21 12:14:16

import netCDF4
# from pyhdf.SD import SD, SDC

def main():
	# url = r"http://hydro1.sci.gsfc.nasa.gov/dods/GLDAS_NOAH025SUBP_3H"
	url = r"https://hs3.nsstc.nasa.gov/thredds/dodsC/pub/HIWRAP/data/2013-09-25/HS3_HIWRAP_20130925_kuouterchirp_185856-191558_v03.nc?alt[0:1:62750],dopcorr[0:1:0][0:1:0]"
	dataset = netCDF4.Dataset(url)

	print dataset.title

	variables = dataset.variables
	variable_list = [key for key in variables.keys()]
	print "variables: ", variables.keys()
	# vt = variables["time"]
	# print vt[:]
	# print vt.shape
	# print type(vt)

	print dir(dataset)


def main():
	pass


if __name__ == '__main__':
	main()