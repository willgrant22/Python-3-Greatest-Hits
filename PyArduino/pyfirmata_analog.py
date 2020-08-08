#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import pyfirmata
import time
 
board = pyfirmata.Arduino('/dev/tty.usbmodem14401')
 
it = pyfirmata.util.Iterator(board)
it.start()
 
analog_input = board.get_pin('a:0:i')
 
while True:
    analog_value = analog_input.read()
    print(analog_value)
    time.sleep(0.1)