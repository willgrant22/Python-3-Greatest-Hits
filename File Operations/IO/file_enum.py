#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 01/27/2020
# Description : enum example
# =============================================================================
# Imports
# =============================================================================

# Initialize list
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

# Enumerate and print lists
for i, color in enumerate(colors):
    ratio = ratios[i]
    print(f'{ratio * 100}% {color}')