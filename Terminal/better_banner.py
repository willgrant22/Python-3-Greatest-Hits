#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os
rows, columns = os.popen('stty size', 'r').read().split()
def headline(**kwargs):
	
	iseven = kwargs['dims']
	text = kwargs['text']
	banner = kwargs['style']

	if banner == 'single':
		response = f"\n{text.title()}\n{'-' * len(text)}\n"
		return response

	elif banner == 'center':
		return f" {text.title()} ".center(50, "o")

	elif banner == 'layer':
		x = int(columns) / 2
		y = len(text.title())
		if iseven == True:
			print(int(x / 0.5))
			if int(y%2) > 0:
				response = f"\n{text.title()}\n".center(int(x / 0.5) + 1, "*")
			else:
				response = f"\n{text.title()}\n".center(int(x / 0.5), "#")
				
		else:
			response = f"\n{text.title()}\n".center(int(x / 0.5 ) + 1, "0")

	return response

def main():
	rows, columns = os.popen('stty size', 'r').read().split()
	col = int(columns)
	row = int(rows)
	dims = int(columns) % 2
	if dims == 1:
		print(headline(dims=False, text='single', style='single'))

		print(f"{headline(dims=False,text='centered', style='center')}")

		print(f"\n{headline(dims=False,text='layered', style='layer')}\n")
		print("odd")
	else:
		print(headline(dims=True, text='single', style='single'))

		print(f"{headline(dims=True,text='centered', style='center')}")

		print(f"\n{headline(dims=True,text='layered', style='layer')}\n")
		print("even")

main()