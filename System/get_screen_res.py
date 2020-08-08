#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pymouse import PyMouse
m = PyMouse()
a,b = m.screen_size()

print(a, b)