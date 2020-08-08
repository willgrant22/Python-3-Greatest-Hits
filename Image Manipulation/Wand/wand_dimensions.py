#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from __future__ import print_function
from wand.image import Image

with Image(filename='test.png') as img:
    print('width =', img.width)
    print('height =', img.height)