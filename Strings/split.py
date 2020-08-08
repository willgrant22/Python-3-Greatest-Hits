#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import re

#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)