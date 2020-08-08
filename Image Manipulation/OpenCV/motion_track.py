#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import cv2, sys

first_frame = None
status_list = [None, None]
img_counter = 1

video = cv2.VideoCapture(int(sys.argv[1]))

width = int(video.set(3, 640))
height = int(video.set(4, 480))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 120.0, (width, height))

a = 1
while True:
    a = a + 1
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    th_delta = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    th_delta = cv2.dilate(th_delta, None, iterations=0)
    (cnts, _) = cv2.findContours(th_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    out.write(frame)
    cv2.imshow('Capturing', frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = f"Motion_Detect_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f'{img_name} written!')
        img_counter += 1
        pass

video.release()
cv2.destroyAllWindows()

