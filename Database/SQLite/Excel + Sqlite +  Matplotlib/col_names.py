#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import sqlite3

# Made function
def col_names():
	db = 'test.db'
	table_name = 'TEST'
	conn = sqlite3.connect(f'{db}')
	cursor = conn.cursor()

	act = "SELECT name FROM PRAGMA_TABLE_INFO('TEST')"
	cursor.execute(act)

	rows = cursor.fetchall()
	oneRow = []
	for row in rows:
		oneRow.append(row)
		print(row)

	length = len(rows)
	y = length + 1
	print(y)

	print(oneRow[0])
	print(''.join(oneRow[0]))

	conn.commit()
	conn.close()


col_names()