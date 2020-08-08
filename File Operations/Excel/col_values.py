#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import xlrd
from datetime import datetime
import xlsxwriter
workbook = 'any.xlsx'
def readCol(): 
	wb = xlrd.open_workbook(workbook) 
	sheet = wb.sheet_by_index(0) 
	sheet.cell_value(0, 0)
	  
	for i in range(sheet.nrows): 
	    print(sheet.cell_value(i, 0, format3))

readCol()