# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-13 11:10:36
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-13 15:20:05


""" nc file dump and extract variables """
import os
from scipy.io import netcdf
# import netCDF4

UPLOADS = "../test/air.sig995.2012.nc"
UPLOADS = "../../DarkData/DataTypes/nc_type/20130425120000-UKMO-L4_GHRSST-SSTfnd-OSTIA-GLOB-v02.0-fv02.0.nc"

f = netcdf.netcdf_file(UPLOADS, 'r')

print dir(f)
print "desc:", f.description
print "dime:", f.dimensions
print "file:", f.filename
print "hist:", f.history
print "plat:", f.platform
print "titl:", f.title
print "vari:", f.variables
print "vers:", f.version_byte


# air = f.variables['air']
# print air.units


# dataset = netCDF4.Dataset(file_path, mode='r')
# print dataset.title