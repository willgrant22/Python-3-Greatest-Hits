#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

from Arduino import Arduino
import time

#tty.usbmodem14401 uno
#tty.wchusbserial1440 nano
board = Arduino(115200, port='/dev/tty.usbmodem14401')

# plugged in via USB, serial com at rate 115200
board.pinMode(13, "OUTPUT")

while True:
	board.digitalWrite(13, "HIGH")
	state_1 = board.digitalRead(13)
	print(state_1)
	board.digitalWrite(13, "LOW") 
	state_2 = board.digitalRead(13)
	print(state_2)