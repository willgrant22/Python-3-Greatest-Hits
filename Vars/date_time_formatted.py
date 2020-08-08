#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 05/16/2020
# Description : Format and print date
# =============================================================================
# Imports
# =============================================================================
from datetime import datetime

# Initialize datetime function
now = datetime.now()

# Format
x = now.strftime("%B %d,%Y %H:%M:%S %p")
y = now.strftime('%m-%d-%Y %I꞉%M꞉%S')

print(f'x = {x}')
print(f'y = {y}')