#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Jason with pandas
# =============================================================================
import pandas as pd 

df = pd.read_json(r'panda.json')

print('\n')
print(df)
print('\n')
print(f'Row 0 ',df['Product'][0], df['Price'][0])

