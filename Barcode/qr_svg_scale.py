#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import pyqrcode 

# Initialize qr data 
s = "test"

# Generate QR code by the help of create function 
url = pyqrcode.create(s) 

# saving the svg file naming "qr.svg" 
url.svg("myqr.svg", scale = 5)

#1 = 29px 29px
#2 = 58px 58px
#3 = 87px 87px
