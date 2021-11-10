#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
# others ███▓▒░░._____.░░▒▓███►
import os, sys

nline = '\n'
ntab = '\t'
ncr = '\r'

lbox = '░'
mbox = '▓'
sbox = '█'
sline = '_'
star = '*'

def TermDims():
	columns, rows = os.get_terminal_size()
	return columns, rows

def headline(**kwargs):
	col, row = TermDims()
	response = ""
	text = kwargs['text']
	banner = kwargs['style']
	argnum = kwargs['argcount']
	
	# single
	if banner == '-s':
		response = f"{nline}{text.title()}{nline}{'-' * len(text)}"
		return response

	# center
	elif banner == '-c':
		return f"{nline}{text.title()} ".center(col, "o")

	# layer
	elif banner == '-l':
		x = col
		y = len(text.title())
		
		place = ((col - int(len(text.title()))) * 0.22)
		total = round(place / 3.4) 

		if int(y%2) > 0:
			response = (
				f"{lbox * x}{ncr}{nline}"
				f"{nline}{ntab * total}{text}{nline}{ncr}"
				f"{nline}{lbox * x}"
				f"{nline}"
				)
		else:
			response =(
				f"{nline}{text.title()}{nline}".center(col * 2, "#")

				) 
	else:
		response = "incorrect"

	return response

def main(argv):
	argnum = len(argv)
	userText = argv[1]
	bannerType = argv[2]
	bannerArgs = headline(text=f'{userText}', style=f'{bannerType}', argcount=f'{argnum}')

	print(bannerArgs)
		
if __name__ == '__main__':
	main(sys.argv)