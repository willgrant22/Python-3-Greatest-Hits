#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 03/22/2020
# Description : Resize image with pil
# =============================================================================
# Imports
# =============================================================================
from PIL import Image

# Load image
im = Image.open('test.jpg')

# Get size
w, h = im.size
print('Original image size: %sx%s' % (w, h))

# Resize
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

# Save in specified format
im.save('thumbnail.jpg', 'jpeg')
