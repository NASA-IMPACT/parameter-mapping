# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-07-13 15:18:04
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-07-13 15:18:33

from pyhdf import SD 		#hdf4


#hdf4
hdf4 = SD.SD(file_path, SD.SDC.READ)
print hdf4.datasets()
print dir(hdf4)
print hdf4.info()
print dir(hdf4.attr())