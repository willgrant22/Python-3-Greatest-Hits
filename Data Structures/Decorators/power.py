#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

class Power(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, *param_arg):
		
		if len(param_arg) == 1:
			def wrapper(a, b):
				retval = param_arg[0](a, b)
				return retval ** self._arg
			return wrapper
		else:
			expo = 2
			retval = self._arg(param_arg[0], param_arg[1])
			return retval ** expo