#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
import qrcode

img = qrcode.make('test text')

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>


img.save('qrcode_test.png')