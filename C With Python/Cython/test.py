#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import run_python
import run_cython
import time

number = 100

start = time.time()
run_python.test(number)
end =  time.time()

py_time = (end - start)
f_py_time = "{0:.10f}".format(py_time)
print(f"Python time = {py_time}")

start = time.time()
run_cython.test(number)
end =  time.time()

cy_time = (end - start)
f_cy_time = "{0:.10f}".format(cy_time)
print(f"Cython time = {cy_time}")

print(f"Speedup = {(py_time / cy_time) / 1}")