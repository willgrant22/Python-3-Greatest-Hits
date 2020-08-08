#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from wand.image import Image

with Image(filename="test.png") as left:
    with left.clone() as right:
        right.enhance()
        left.extent(width=left.width*2)
        left.composite(right, top=0, left=right.width)
    left.save(filename="test-enhance.png")