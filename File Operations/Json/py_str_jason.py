#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=4)

# the result is a JSON string:
print(y)