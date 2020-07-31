#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import qrcode
import qrcode.image.svg

method = "basic"

data = "Some text that you want to store in the qrcode"

if method == 'basic':
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    factory = qrcode.image.svg.SvgFragmentImage
elif method == 'path':
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make(data, image_factory = factory)

img.save("qrcode.svg")