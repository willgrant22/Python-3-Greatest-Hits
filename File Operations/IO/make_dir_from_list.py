#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os
import sys

folders_to_be_made = ('azteccodecompact','aztecrune','bc412',
        'channelcode','codablockf','code11','code128',
        'code16k','code2of5','code32','code39','code39ext',
        'code49','code93','code93ext','codeone','coop2of5',
        'daft','databarexpanded','databarlimited',
        'databaromni','databarstacked','datalogic2of5',
        'datamatrix','datamatrixrectangular',
        'datamatrixrectangularextension','dotcode',
        'ean13','ean13composite','ean14','ean2','ean5',
        'ean8','ean8composite','flattermarken','hanxin',
        'hibcazteccode','hibccodablockf','hibccode128',
        'hibccode39','hibcdatamatrix',
        'hibcdatamatrixrectangular','hibcmicropdf417',
        'hibcpdf417','hibcqrcode','iata2of5','identcode',
        'industrial2of5','interleaved2of5','isbn','ismn',
        'issn','itf14','jabcode','japanpost','kix',
        'leitcode','mailmark','matrix2of5','maxicode',
        'micropdf417','microqrcode','msi','onecode',
        'pdf417','pdf417compact','pharmacode','pharmacode2',
        'planet','plessey','posicode','postnet','pzn',
        'qrcode','rationalizedCodabar','raw','royalmail',
        'sscc18','symbol','telepen','telepennumeric',
        'ultracode','upca','upce')

cwd = os.getcwd()
for i in range(len(folders_to_be_made)):
	d = os.path.join(f'{cwd}/barcodes/{folders_to_be_made[i]}')
	if not os.path.exists(d):
		os.makedirs(d)