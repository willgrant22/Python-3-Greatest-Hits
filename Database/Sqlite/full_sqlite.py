#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 06/11/2019
# Description : Create/Insert into sqlite
# =============================================================================
# Imports
# =============================================================================
import sqlite3

# Create table class
class createTbl:
    # Open database
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    # Create table
    def createSysTbl():
        createTbl.conn.execute(''' CREATE TABLE TEST
	    	(ID INT PRIMARY KEY		NOT NULL,
	    	PURPOSE		TEXT	NOT NULL,
	    	CMD		    TEXT	NOT NULL,
	    	NAME      	TEXT	NOT NULL);''')
# Insert data class
class insertDat:
    # Open database
    conn = sqlite3.connect('test.db')
    print("Data added successfully")
    # Insert data into created table
    def insertSysCmd():
        conn = sqlite3.connect('test.db')
        conn.execute("INSERT INTO TEST (ID, PURPOSE, CMD, NAME) \
        VALUES (1, 'purpose', 'name', 'word')");

createTbl.createSysTbl()
createTbl.conn.commit()
createTbl.conn.close()

insertDat.conn.commit()
insertDat.conn.close() 

