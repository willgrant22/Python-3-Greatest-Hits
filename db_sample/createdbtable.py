#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");
def createTbl():
    conn.execute('''CREATE TABLE COMMANDS
    (ID     INT PRIMARY KEY    NOT NULL,
     PURPOSE           TEXT    NOT NULL,
     NAME	           TEXT    NOT NULL,
     COMMAND           TEXT    NOT NULL);''')
    print ("Table created successfully");

createTbl()
conn.close()