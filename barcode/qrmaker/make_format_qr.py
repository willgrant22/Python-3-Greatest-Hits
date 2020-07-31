#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import qrcode
import os

def make_qr():
	with open ("passwords.txt", "r") as fileHandler:
		i = 0
		for line in fileHandler:
			i = i + 1
			img = qrcode.make(line.strip())
			img.save(f'qrcodes/qr_{i}.png')

def rename_qr():
	with open ("username.txt", "r") as fileHandler:
		i = 0
		for line in fileHandler:
			i = i + 1
			uname = line.strip()
			src =(f'qrcodes/qr_{i}.png') 
			dst =(f'qrcodes/qr_{uname}.png') 
			os.rename(src, dst)

def main():
	make_qr()
	rename_qr()

main()
