#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from openpyxl import Workbook
wb = Workbook()
ws = wb.active
print(wb, ws)

ws.title = "New Title"
ws.sheet_properties.tabColor = "1072BA"
ws3 = wb["New Title"]

print(wb.sheetnames)

for sheet in wb:
	print(sheet.title)

source = wb.active
target = wb.copy_worksheet(source)