#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import xlrd, sqlite3

databaseLocation = ('data.xlsx')
wb = xlrd.open_workbook(databaseLocation)
sheet = wb.sheet_by_index(0)
sheet.cell_value(1, 2)
rows = sheet.nrows
print(rows)

def createTBL():
	db = 'data.db'
	conn = sqlite3.connect(f'{db}')
	conn.execute('''CREATE TABLE IF NOT EXISTS DATA
	(ROW INTEGER PRIMARY KEY NOT NULL UNIQUE,
	SDATE			 TEXT NOT NULL,
	USERNAME TEXT NOT NULL,
	DSALES 	 INTEGERNOT NULL ,
	SALEVALINTNOT NULL);''')
	conn.commit()

def fromExcel():
	s=[]
	u=[]
	sd=[]
	sv=[]

	data = []

	for i in range(rows):
		sdate = sheet.cell_value(i, 0)
		userN = sheet.cell_value(i, 1)
		dsales = sheet.cell_value(i, 2)
		saleval = sheet.cell_value(i, 3)

		sd.append(sdate)
		u.append(userN)
		s.append(dsales)
		sv.append(saleval)

	conn = sqlite3.connect(f'data.db')
	cursor = conn.cursor()

	for j in range(rows):
		insert = "INSERT INTO data (SDATE, USERNAME, DSALES, SALEVAL) \
			VALUES (?,?,?,?)"

		data = sd[j], u[j], s[j], sv[j]
		cursor.execute(insert, data)
		conn.commit()

	conn.close()


def main():
	createTBL()
	fromExcel()

main()
