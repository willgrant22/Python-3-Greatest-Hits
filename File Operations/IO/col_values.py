#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 03/18/2020
# Description : Get spreadsheet col values
# =============================================================================
# Imports
# =============================================================================
import xlrd 

# Give the location of the file 
loc = ('passwords.xlsx') 

# Open file and set col range
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(3, 1) 

# Print col val
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))
