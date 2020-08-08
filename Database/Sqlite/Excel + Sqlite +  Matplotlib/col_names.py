#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

db = 'test.db'
table_name = 'TEST'
conn = sqlite3.connect(f'{db}')
cursor = conn.cursor()

act = "SELECT name FROM PRAGMA_TABLE_INFO('TEST')"
cursor.execute(act)

rows = cursor.fetchall()
oneRow = cursor.fetchone()
print(oneRow[0])
for row in rows:
	print(row)

length = len(rows)
print('\n')	
print(f'The list length is: {length}')
y = length + 1
print(y)

conn.commit()
conn.close()