#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import qrcode
import qrcode.image.svg

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

data = "Some text that you want to store in the qrcode"

qr.add_data(data)
qr.make(fit=True)

img = qrcode.make(data, image_factory = factory)

img.save("qrcode.svg")