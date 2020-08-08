#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

class Database:
	db = 'password.db'
	positiveConO = 'Database has been opened successfully!'
	positiveConC = 'Database has been closed successfully!'
	positiveTbl = 'Table created successfully'
	positiveIn = 'Records created successfully!'

	def __init__(self, service, username, password):
		self.service = service
		self.username = username
		self.password = password

		Database.db = self.db
		Database.positiveConO = self.positiveConO
		Database.positiveConC = self.positiveConC
		Database.positiveTbl = self.positiveTbl
		Database.positiveIn = self.positiveIn
		
	def createTBL(self):
		conn = sqlite3.connect(f'{self.db}')
		print(self.positiveConO)
		conn.execute('''CREATE TABLE IF NOT EXISTS PASSWORDS
		(ROW INTEGER PRIMARY KEY     NOT NULL UNIQUE,
		SERVICE           TEXT    NOT NULL UNIQUE,
		USERNAME           TEXT    NOT NULL,
		PASSWORD            TEXT     NOT NULL);''')
		
		print (self.positiveTbl);
		conn.commit()
		conn.close()

	def insertData(self):
		conn = sqlite3.connect(f'{self.db}')
		cursor = conn.cursor()
		insert = f"INSERT INTO PASSWORDS (SERVICE, USERNAME, PASSWORD) \
			VALUES (\'{self.service}\', \'{self.username}\', \'{self.password}\')";
		
		cursor.execute(insert)
		conn.commit()
		print(self.positiveIn)
		conn.close()
		print(self.positiveConC)

	def queryData(self):
		conn = sqlite3.connect(f'{self.db}')
		cursor = conn.cursor()
		serv = 'service'
		
		oppUp = f'UPDATE PASSWORDS SET SERVICE="{serv}" WHERE ROW = 2'
		oppDel = 'DELETE SERVICE FROM PASSWORDS WHERE ROW = 1'
		oppCol = 'SELECT SERVICE, USERNAME FROM PASSWORDS'
		oppAll = 'SELECT * FROM PASSWORDS'
		opp = 'SELECT * FROM PASSWORDS WHERE ROW = 2'

		cursor.execute(oppDel)

		results = cursor.fetchall()

		for row in results:
			print('\n', 'Length: ', len(row), '\n')
			print(row)

		conn.commit()
		conn.close()

