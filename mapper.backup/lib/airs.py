#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ritesh
# @Date:   2015-12-10 16:37:35
# @Last Modified by:   ritesh
# @Last Modified time: 2015-12-10 18:48:02

AIRS_KEYWORDS = [
	"ATMOSPHERE->AIRQUALITY->CARBONMONOXIDE",
	"ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE",
	"ATMOSPHERE->ALTITUDE->GEOPOTENTIALHEIGHT",
	"ATMOSPHERE->ALTITUDE->TROPOPAUSE",
	"ATMOSPHERE->ATMOSPHERICTEMPERATURE->SURFACEAIRTEMPERATURE",
	"ATMOSPHERE->ATMOSPHERICTEMPERATURE->TEMPERATUREPROFILES",
	"ATMOSPHERE->ATMOSPHERICWATERVAPOR->PRECIPITABLEWATER",
	"ATMOSPHERE->ATMOSPHERICWATERVAPOR->WATERVAPORPROFILES",
	"ATMOSPHERE->ATMOSPHERICCHEMISTRY->CARBONANDHYDROCARBONCOMPOUNDS->METHANE",
	"ATMOSPHERE->ATMOSPHERICCHEMISTRY->SULFURCOMPOUNDS->SULFURDIOXIDE",
	"ATMOSPHERE->CLOUDS->CLOUDPROPERTIES->CLOUDFRACTION",
	"ATMOSPHERE->CLOUDS->CLOUDPROPERTIES->CLOUDFREQUENCY",
	"ATMOSPHERE->CLOUDS->CLOUDPROPERTIES->CLOUDTOPPRESSURE",
	"ATMOSPHERE->CLOUDS->CLOUDPROPERTIES->CLOUDTOPTEMPERATURE"
	]


AIRS_VARIABLES = [
	"latAIRS",
	"lonAIRS",
	"TAirStd",
	"TAirStd_QC",
	"TAirStdErr",
	"TSurfAir",
	"GP_Height",
	"GP_Height_QC",
	"TAirStd_QC",
	"TAirStdErr",
	"TSurfAir",
	"PCldTop",
	"PCldTop_QC",
	"PCldTopErr",
	"TCldTop"
]

import random
AIRS_MAP = dict()
for k in AIRS_KEYWORDS:
	AIRS_MAP[k] = random.sample(AIRS_VARIABLES, random.randint(1,4))


class Lookup(dict):
    """
    a dictionary which can lookup value by key, or keys by value
    """
    def __init__(self, items=[]):
        """items can be a list of pair_lists or a dictionary"""
        dict.__init__(self, items)

    def get_key(self, value):
        """find the key(s) as a list given a value"""
        return [k for k,v in self.iteritems() if value in v]

    def get_value(self, key):
        """find the value given a key"""
        return self[key]

def main():
	print AIRS_MAP
	lookup = Lookup(AIRS_MAP)

	print "K-V: (ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE)"
	print lookup.get_value("ATMOSPHERE->AIRQUALITY->TROPOSPHERICOZONE")
	print "V-K: (PCldTop)"
	print lookup.get_key("PCldTop")

if __name__ == '__main__':
	main()