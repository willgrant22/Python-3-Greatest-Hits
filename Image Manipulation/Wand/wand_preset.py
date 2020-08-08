#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from wand.image import Image

with Image(width=100, height=100, pseudo='plasma:') as img:
    img.save(filename='100x100-plasma.png')