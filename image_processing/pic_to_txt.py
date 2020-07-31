#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Get text from picture
# =============================================================================
# Imports
# =============================================================================
import cv2 
import pytesseract 

# Initialize photo
img = cv2.imread("image.png") 
# Extract text from picture
text = pytesseract.image_to_string(img)
with open('test.txt',mode ='w') as file:
                 file.write(text) 
            