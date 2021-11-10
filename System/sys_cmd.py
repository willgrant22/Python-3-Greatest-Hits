#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import subprocess
import sys
import py_template

x = str(sys.argv[1])


py_template.simpleMain(x)
test = subprocess.Popen(["open",f'{x}.py'], stdout=subprocess.PIPE)
output = test.communicate()[0]

del(x,test,output)