#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import pyfirmata
import time
 
board = pyfirmata.Arduino('/dev/tty.wchusbserial1440')
 
it = pyfirmata.util.Iterator(board)
it.start()
 
digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')
 
while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)