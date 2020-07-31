#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import sqlite3

def Database(func):
	def wrapper(**kwargs):
		conn = sqlite3.connect(f"{kwargs['database']}.db")
		func(**kwargs)
		d = kwargs['database']
		conn.commit()
		conn.close()
	return wrapper

def InsertData(func):
	def wrapper(**kwargs):
		db = kwargs['database']
		table = kwargs['table']
		daydate = kwargs['date']
		recby = kwargs['recby']
		track = kwargs['trk']
		po = kwargs['po']
		shipper = kwargs['shpr']
		delto = kwargs['delto']

		conn = sqlite3.connect(f"{kwargs['database']}.db")
		cursor = conn.cursor()

		insertion = f"INSERT INTO {table} (DAYDATE, RECIEVEDBY, TRACKING, PO, SHIPPER, DELIVEREDTO) \
			VALUES (?,?,?,?,?,?)"

		data = daydate, recby, track, po, shipper, delto

		cursor.execute(insertion, data)
		
		func(**kwargs)
		print(daydate, recby, track, po, shipper, delto)

		conn.commit()
		conn.close()
	return wrapper

def CreateTbl(func):
	def wrapper(**kwargs):
		db = kwargs['database']
		table = kwargs['table']

		conn = sqlite3.connect(f"{db}.db")
		conn.execute(f'''CREATE TABLE IF NOT EXISTS {table}
		(ROW INTEGER PRIMARY KEY     NOT NULL UNIQUE,
		DAYDATE   		     TEXT    NOT NULL,
		RECIEVEDBY           TEXT    NOT NULL,
		TRACKING			 TEXT	 NOT NULL UNIQUE,
		PO 					 INT     NOT NULL,
		SHIPPER              TEXT    NOT NULL,
		DELIVEREDTO          TEXT     NOT NULL);''')

		func(**kwargs)

		conn.commit()
		conn.close()
	return wrapper