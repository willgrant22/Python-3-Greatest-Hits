#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import pyqrcode 
import png 
from pyqrcode import QRCode 

s = "https://www.google.com/"

url = pyqrcode.create(s) 

url.svg("myqr.svg", scale = 14) 

url.png('myqr.png', scale = 6) 

