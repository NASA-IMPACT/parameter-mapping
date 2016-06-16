#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2016-01-26 15:01:12
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-06-16 15:07:38

ACRONYMS = dict(
	res 			= "resolution",
	sst 			= "sea_surface_temperature",
	med 			= "medium ",
	temp 			= "temperature",
	cld 			= "cloud",
	pres 			= "pressure",
	rh 				= "relative_humidity",
	relh 			= "relative_humidity",
	pbl 			= "planetary_boundary_layer",
	aod 			= "aerosol_optical_depth",
	aot 			= "aerosol_optical_thickness",
	o3 				= "ozone",
	h2o 			= "water",
	tsurfair 		= "temperature_surface_air",
	tsurfstd		= "temperature_surface_standard",
	tairstd			= "temperature_air_standard",
	tairstderr		= "temperature_air_standard_error",
	gp 				= "geopotential",
	lis				= "lightning_imaging_sensor",
	otd				= "optical_transient_detector",
	li 				= "lightning_imaging"
	)

DISCARDS = ["lat", "lon", "latitude", "longitude", "rank", "total", "processing_flag", "k_index", "time", "flag", "quality"]
