#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import xlrd 

loc = "May.xlsx"
def colN(self):
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	  
	# row 0 and column 0 
	sheet.cell_value(0, 0) 
	  
	for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 

