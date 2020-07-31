#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

class createTbl:
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    def createSysTbl():
        createTbl.conn.execute(''' CREATE TABLE SYSCOMMANDS
	    	(ID INT PRIMARY KEY		NOT NULL,
	    	PURPOSE		TEXT	NOT NULL,
	    	TESTCMD		TEXT	NOT NULL,
	    	UBUNTUCMD	TEXT	NOT NULL);''')

        createTbl.conn.commit()
        createTbl.conn.close()

    def createMainTbl():
        createTbl.conn.execute(''' CREATE TABLE MAINCOMMANDS
        	(ID INT PRIMARY KEY     NOT NULL,
        	PURPOSE     TEXT    NOT NULL,
        	TESTCMD     TEXT    NOT NULL,
        	DEFCALL     TEXT    NOT NULL);''')

        createTbl.conn.commit()
        createTbl.conn.close()

    def createNetTbl():
    	createTbl.conn.execute(''' CREATE TABLE NETCOMMANDS
    		(ID INT PRIMARY KEY		NOT NULL,
    		PURPOSE		TEXT	NOT NULL,
    		TESTCMD		TEXT	NOT NULL,
    		DEFFCALL	TEXT	NOT NULL);''')

        createTbl.conn.commit()
        createTbl.conn.close()  	

    def createToolTbl():
    	createTbl.conn.execute(''' CREATE TABLE TOOLCOMMANDS
    		(ID INT PRIMARY KEY		NOT NULL,
    		PURPOSE		TEXT	NOT NULL,
    		TESTCMD		TEXT	NOT NULL,
    		DEFFCALL	TEXT	NOT NULL);''')

        createTbl.conn.commit()
        createTbl.conn.close()

class insertDat:
    conn = sqlite3.connect('test.db')
    print("Data added successfully")

    def insertSysCmd():
        conn.execute("INSERT INTO COMMANDS (ID,PURPOSE,TESTCMD,UBUNTUCMD) \
        VALUES (1, 'purpose', 'name', 'word')");

        insertDat.conn.commit()
        insertDat.conn.close()   

createTbl.createSysTbl()
createTbl.createMainTbl()
createTbl.createNetTbl()
createTbl.createToolTbl()
insertDat.insertSysCmd()

