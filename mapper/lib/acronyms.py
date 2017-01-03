#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-01-26 15:01:12
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-08-24 01:37:34

ACRONYMS = dict(
	res 			= "resolution",
	sst 			= "sea surface temperature",
	med 			= "medium ",
	temp 			= "temperature",
	cld 			= "cloud",
	pres 			= "pressure",
	rh 				= "relative humidity",
	relh 			= "relative humidity",
	pbl 			= "planetary boundary layer",
	aod 			= "aerosol optical depth",
	aot 			= "aerosol optical thickness",
	o3 				= "ozone",
	h2o 			= "water",
	tsurfair 		= "temperature surface air",
	tsurfstd		= "temperature surface standard",
	tairstd			= "temperature air standard",
	tairstderr	= "temperature air standard error",
	gp 				= "geopotential",
	lis				= "lightning imaging sensor",
	otd				= "optical transient detector",
	li 				= "lightning imaging",
	precip		= "precipitation",
	tot				= "total",
	o2				= "molecular oxygen",
	so4				= "sulfate",
	dms				= "dimethyl sulfide",
	so2				= "sulfur dioxide",
	carbon 	  = "carbonaceous",
	swe 			= 'snow water equivalent',
	si        = 'sea ice'
	)

DISCARDS = ["lat", "lon", "latitude", "longitude", "rank", "index", "time", "flag", "quality", "qual", 'qa', 'flags']
