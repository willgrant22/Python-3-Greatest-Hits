#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import json
from vultr import Vultr

api_key = ''
vultr = Vultr(api_key)
plans_json = vultr.plans.list()

with open('data.json', 'w', encoding='utf-8') as formattedJson:
    json.dump(plans_json, formattedJson, ensure_ascii=False, sort_keys=True, indent=2, skipkeys=True, separators=(',\n', ':'))
    
with open('data.json', 'r') as readGet:
	data = json.load(readGet)
print(data['118']['available_locations'])

with open('unfmt.json', 'w') as unformattedJson:
	json.dump(data, unformattedJson)
print(data)
