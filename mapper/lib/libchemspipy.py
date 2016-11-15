# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-08-24 00:59:17
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-08-24 01:08:05

from chemspipy import ChemSpider
cs = ChemSpider('26d2a19a-9226-4ff0-a9e1-4424ca8ec286')


def get_common_name(formula):
	results = cs.simple_search(formula)
	if len(results) > 1:
		return ' '.join([result.common_name for result in results])
	else:
		return None
