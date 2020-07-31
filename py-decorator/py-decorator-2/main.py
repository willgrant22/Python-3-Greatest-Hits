#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

from mailtrans import table_it, create_it, insert_it
'''
a = create_it(transaction=1, database='kk')
'''

'''
b = table_it(

		transaction=2,
		database='TEST',
		table='TESTTBL',
		date='07/03/2020',
		recby='will g.',
		trk='1z234h3g23',
		po='104344534',
		shpr='ups',
		delto='john s.'

		)
'''

c = insert_it(

		transaction=2,
		database='TEST',
		table='TESTTBL',
		date='07/03/2020',
		recby='will g.',
		trk='1z234h3g23',
		po='104344534',
		shpr='ups',
		delto='john s.'

		)

del c