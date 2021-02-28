#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

total = 0

def sum( arg1, arg2 ):

   total = arg1 + arg2;
   print ("Inside the function local total : ", total)
   return total

sum( 10, 20 )
print ("Outside the function global total : ", total )