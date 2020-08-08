#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import qrcode
from PIL import Image

img_bg = Image.open('pic.jpg')

qr = qrcode.QRCode(box_size=5)
qr.add_data('I am qr')
qr.make()
img_qr = qr.make_image()

pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

img_bg.paste(img_qr, pos)
img_bg.save('qr_m.png')