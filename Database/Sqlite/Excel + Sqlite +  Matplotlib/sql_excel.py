#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import xlrd
from db_class import *

loc = ('passwords.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(1, 2)

def createTBL():
	db = 'password.db'
	conn = sqlite3.connect(f'{db}')
	conn.execute('''CREATE TABLE IF NOT EXISTS PASSWORDS
	(ROW INTEGER PRIMARY KEY     NOT NULL UNIQUE,
	SERVICE           TEXT    NOT NULL ,
	USERNAME           TEXT    NOT NULL,
	PASSWORD            TEXT     NOT NULL);''')

	conn.commit()

def fromE():
	p=[]
	u=[]
	s=[]
	data = []
	for i in range(1, 35):
		passW = sheet.cell_value(i, 2)
		userN = sheet.cell_value(i, 1)
		serv = sheet.cell_value(i, 0)

		s.append(serv)
		u.append(userN)
		p.append(passW)

	conn = sqlite3.connect(f'password.db')
	cursor = conn.cursor()

	for j in range(0,34):
		insert = "INSERT INTO PASSWORDS (SERVICE, USERNAME, PASSWORD) \
			VALUES (?,?,?)"

		data = s[j], u[j], p[j]
		cursor.execute(insert, data)
		conn.commit()

	conn.close()

def main():
	createTBL()
	fromE()

main()
