#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pyzbar import pyzbar
import cv2

img_path = 'myqr.png'

img = cv2.imread(img_path)

barcodes = pyzbar.decode(img)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), 1)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = f"{barcodeData} ({barcodeType})"
    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    print(f"[INFO] found {barcodeType} barcode {barcodeData}")

cv2.imwrite("new_img.png", img)