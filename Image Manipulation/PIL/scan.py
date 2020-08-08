#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from sys import argv
import zbar
import Image

if len(argv) < 2: exit(1)

scanner = zbar.ImageScanner()

scanner.parse_config('enable')

pil = Image.open(argv[1]).convert('L')
width, height = pil.size
raw = pil.tostring()

image = zbar.Image(width, height, 'Y800', raw)

scanner.scan(image)

for symbol in image:
    print ('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)

del(image)
