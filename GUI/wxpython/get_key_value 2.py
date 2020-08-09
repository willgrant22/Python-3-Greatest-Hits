#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 03/09/2020
# Description : Get key values for key event
# =============================================================================
# Imports
# =============================================================================
import cv2

# Load image
img = cv2.imread('test.png')

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    # Esc key to stop
    if k==27:
        break
    # normally -1 returned,so don't print it
    elif k==-1:
        continue
    # else print its value
    else:
        print(k)