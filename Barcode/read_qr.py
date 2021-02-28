#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pyzbar import pyzbar
import cv2

img_path = 'qr.png'

# Read image
img = cv2.imread(img_path)

# Initialize barcode decoder
barcodes = pyzbar.decode(img)

# Get and format data
for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), 2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = f"{barcodeData} ({barcodeType})"
    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    print(f"[INFO] found {barcodeType} barcode {barcodeData}")

# Create new photo with data
cv2.imwrite("new_img.png", img)