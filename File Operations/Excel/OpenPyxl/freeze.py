#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from openpyxl import Workbook, load_workbook

workbook = load_workbook(filename="OOM.xlsx")
sheet = workbook.active

sheet.freeze_panes = "C2"
workbook.save("OOM.xlsx")