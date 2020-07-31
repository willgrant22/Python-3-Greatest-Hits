#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import numpy as np
import cv2
from pyzbar import pyzbar
import qrcode
from imutils.video import VideoStream

cap = cv2.VideoCapture(2) 
img_counter = 0
    
width = int(cap.set(3, 100))
height = int(cap.set(4, 200))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x - 15, y - 15), (x + w + 15, y + h + 15), (0, 0, 255), 2)
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = f"{barcodeData} ({barcodeType})"
            cv2.putText(frame, text, (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            print(f"[INFO] found {barcodeType} barcode {barcodeData}")

            out.write(frame)            

        cv2.imshow('frame',frame)
        
        k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = f"label_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

out.release()
cap.release()
cv2.destroyAllWindows()