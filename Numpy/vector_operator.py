#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import numpy as np

matrix = np.array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

mul_5 = lambda x: x * 5
vectorized_mul_5 = np.vectorize(mul_5)

x = vectorized_mul_5(matrix)
print(x)