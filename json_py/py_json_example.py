#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import json

with open('data.json') as f:
  data = json.load(f)

print(data)