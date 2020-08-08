#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
import pyqrcode 
import png 
from pyqrcode import QRCode 


# String which represents the QR code 
s = "test data"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file 
url.svg("qr.svg", scale = 14) 

# Create and save the png file
url.png('qr.png', scale = 6) 

