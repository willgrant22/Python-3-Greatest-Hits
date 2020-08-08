#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import cv2
import numpy as np

im = cv2.imread("test.jpg")

r = cv2.selectROI(im)

imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow("Image", imCrop)
cv2.waitKey(0)