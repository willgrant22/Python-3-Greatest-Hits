#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import qrcode
import qrcode.image.svg

# possible values 'basic' 'fragment' 'path'
method = "basic"

data = "test text"

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
elif method == 'path':
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

# Set data to qrcode
img = qrcode.make(data, image_factory = factory)

# Save svg file somewhere
img.save("qrcode.svg")