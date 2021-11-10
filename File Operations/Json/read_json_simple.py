#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import json

f = open('write.json',)

data = json.load(f)

for i in data['person']:
	print(i)
	print('\n')
	print(i['name'])

f.close()