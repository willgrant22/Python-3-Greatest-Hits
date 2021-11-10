#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import json
from vultr import Vultr

api_key = ''
vultr = Vultr(api_key)
plans_json = vultr.os.list()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(plans_json, f, ensure_ascii=False, sort_keys=True, indent=2, skipkeys=True, separators=(',\n', ':'))
    
with open('data.json', 'r') as f:
	data = json.load(f)

