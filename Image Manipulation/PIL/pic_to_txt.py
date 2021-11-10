#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import cv2 
import pytesseract 

img = cv2.imread("image.png") 

text = pytesseract.image_to_string(img)
with open('test.txt',mode ='w') as file:      
      
                 file.write(text) 
            