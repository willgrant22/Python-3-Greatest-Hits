#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import pyfirmata
import time
 
board = pyfirmata.Arduino('/dev/tty.usbmodem14401')

# Using sleep to blink 
while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)