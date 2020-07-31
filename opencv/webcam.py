#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from imutils.video import VideoStream
import imutils
from pyzbar import pyzbar
import cv2

def show_webcam(mirror=False):
    capture = capture
    ret, frame = capture.read()

    height, width = frame.shape[:2]
    parent.SetSize((width, height))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cam = cv2.VideoCapture(0)

    while True:
        frame = cam.read()
        frame = imutils.resize(frame, width=400)
        original = frame.copy()
        barcodes = pyzbar.decode(frame)
        barcode_num = 0

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            ROI = original[y:y+h, x:x+w]
            cv2.imwrite('barcode_{}.png'.format(barcode_num), ROI)
            barcode_num += 1
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = "{}".format(barcodeData)
            cv2.putText(frame, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            ROI = image[y1:y2, x1:x2]
            cnts = cv2.findContours(cnts, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            ROI_number = 0
            for c in cnts:
                x,y,w,h = cv2.boundingRect(c)
                ROI = image[y:y+h, x:x+w]
                cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
                ROI_number += 1


            if barcodeData not in found:
                csv.write("{}\n".format(barcodeData))
                csv.flush()

                found.clear()
                found.add(barcodeData)

    cv2.imshow("Live Stream Window", frame)
    key = cv2.waitKey(1) & 0xFF

def main():
    show_webcam(mirror=False)

main()