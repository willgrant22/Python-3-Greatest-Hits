#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
#calling
#from fib import fib
#fib(100)
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]