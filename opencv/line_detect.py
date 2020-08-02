#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(2)
img_counter = 1

width = int(cap.set(3, 140))
height = int(cap.set(4, 480))

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (width, height))

while True:
    _, image = cap.read()
    # convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # perform edge detection
    edges = cv2.Canny(grayscale, 60, 200)
    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 2)
    # show images
    out.write(image)
    cv2.imshow("image", image)
    #cv2.imshow("edges", edges)
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = f"Line_Detect_{img_counter}.png"
        cv2.imwrite(img_name, image)
        print(f'{img_name} written!')
        img_counter += 1
        
        pass

cap.release()
cv2.destroyAllWindows()