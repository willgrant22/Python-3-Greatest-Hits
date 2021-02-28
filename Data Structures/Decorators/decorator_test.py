#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import power
from power import Power
@Power
def multiply_together(a, b):
	return a * b


print(multiply_together(2, 2))

''' @Power(3) #cube
def multiply_together(a, b):
	return a * b '''