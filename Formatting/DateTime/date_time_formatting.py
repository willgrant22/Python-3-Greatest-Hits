#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import datetime
from datetime import date

today = date.today()
month = today.month
day = today.day
year = today.year
now = datetime.datetime.now()

allDT = now.strftime("%Y-%m-%d %H:%M:%S")

monthWord = now.strftime("%B")
wbName = (f'{monthWord}_{year}.xlsx')

print('\n')
print(f'{allDT}\n')
print(f'{monthWord}\n')
print(f'{month}-{day}\n')
print(year)
print('\n')
print(f'{wbName}')

