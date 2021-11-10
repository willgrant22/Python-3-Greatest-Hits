#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from vidgear.gears import ScreenGear
import cv2

stream = ScreenGear().start()

while True:

    frame = stream.read()

    if frame is None:
        break
    # {do something with the frame here}
    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()

stream.stop()