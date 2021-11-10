#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import json

with open('read.json', 'r') as f:
    array = f.read()

obj = json.loads(array)

print (obj['questions'][0]['type'])
print (obj['questions'][0]['name'])