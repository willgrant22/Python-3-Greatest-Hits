#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from wand.color import Color
from wand.image import Image

with Color('red') as bg:
    with Image(width=200, height=100, background=bg) as img:
        img.save(filename='200x100-red.png')