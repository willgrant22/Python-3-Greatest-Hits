#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from wand.image import Image

with Image(width=200, height=100) as img:
    img.save(filename='200x100-transparent.png')