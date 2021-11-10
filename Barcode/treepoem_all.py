#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import treepoem

image = treepoem.generate_barcode(
	barcode_type='qrcode',
	data='042100005264',

	options={'includetext': True},
)

image.convert('1').save('barcode_9.png')

"""
Supported barcode types are: auspost, azteccode, azteccodecompact, aztecrune,
bc412, channelcode, codablockf, code11, code128, code16k, code2of5, code32,
code39, code39ext, code49, code93, code93ext, codeone, coop2of5, daft,
databarexpanded, databarexpandedcomposite, databarexpandedstacked,
databarexpandedstackedcomposite, databarlimited, databarlimitedcomposite,
databaromni, databaromnicomposite, databarstacked, databarstackedcomposite,
databarstackedomni, databarstackedomnicomposite, databartruncated,
databartruncatedcomposite, datalogic2of5, datamatrix, datamatrixrectangular,
datamatrixrectangularextension, dotcode, ean13, ean13composite, ean14, ean2, ean5,
ean8, ean8composite, flattermarken, gs1-128, gs1-128composite, gs1-cc,
gs1datamatrix, gs1datamatrixrectangular, gs1northamericancoupon, gs1qrcode,
hanxin, hibcazteccode, hibccodablockf, hibccode128, hibccode39, hibcdatamatrix,
hibcdatamatrixrectangular, hibcmicropdf417, hibcpdf417, hibcqrcode, iata2of5,
identcode, industrial2of5, interleaved2of5, isbn, ismn, issn, itf14, jabcode,
japanpost, kix, leitcode, mailmark, matrix2of5, maxicode, micropdf417,
microqrcode, msi, onecode, pdf417, pdf417compact, pharmacode, pharmacode2, planet,
plessey, posicode, postnet, pzn, qrcode, rationalizedCodabar, raw, royalmail,
sscc18, symbol, telepen, telepennumeric, ultracode, upca, upcacomposite, upce,
upcecomposite
"""