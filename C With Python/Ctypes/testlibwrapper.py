#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import ctypes

testlib = ctypes.CDLL('testlib.so')
testlib.myprint()