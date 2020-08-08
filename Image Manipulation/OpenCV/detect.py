#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import cv2
import argparse
import os

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = x
        self.width  = width
        self.height = height

def detect_box(image, win_name="window (hit q to exit)"):
    box_defined = False
    box = Rect(0, 0, 0, 0)
    def define_box(event, x, y, flags, param):

        nonlocal box_defined, box
        if event == cv2.EVENT_LBUTTONDOWN:
            box_defined = False
            box.x = x
            box.y = y
            box.width  = 0
            box.height = 0

        if event == cv2.EVENT_MOUSEMOVE:
            if not box_defined:
                box.width  = x - box.x
                box.height = y - box.y

        if event == cv2.EVENT_LBUTTONUP:
            box_defined = True

    def do_nothing(event, x, y, flags, param):
        pass

    cv2.setMouseCallback(win_name, define_box)

    while True:
        clone = image.copy()
        if box.x > 0 and box.width > 0:

            p0 = (box.x, box.y)
            p1 = (box.x + box.width, box.y + box.height)
            cv2.rectangle(clone, p0, p1, (0, 255, 0), thickness=2)

        cv2.imshow(win_name, clone)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

    cv2.setMouseCallback(win_name, do_nothing)

    return box

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image path.")
args = vars(ap.parse_args())

image_path = args['image']

image = cv2.imread(image_path)

win_name = 'window (hit q to exit)'
cv2.namedWindow(win_name)

box = detect_box(image, win_name)

print("Box: ({}, {}, {}, {}) ".format(box.x, box.y, box.width, box.height))

cv2.destroyAllWindows()
