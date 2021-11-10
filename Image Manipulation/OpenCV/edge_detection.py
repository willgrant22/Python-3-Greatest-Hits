#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import numpy as np
import cv2, sys

cap = cv2.VideoCapture(int(sys.argv[1]))
img_counter = 1


width = int(cap.set(3, 640))
height = int(cap.set(4, 480))

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
out = cv2.VideoWriter('output.mp4', fourcc, 120.0, (width, height))

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)

    out.write(edges)
    cv2.imshow("edges", edges)
    #cv2.imshow("gray", gray)
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = f"Edge_Detect_{img_counter}.png"
        cv2.imwrite(img_name, edges)
        print(f'{img_name} written!')
        img_counter += 1
        pass

cap.release()
cv2.destroyAllWindows()