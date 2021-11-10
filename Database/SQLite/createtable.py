#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 11/30/2018
# Description : Create sqlite table
# =============================================================================
# Imports
# =============================================================================

import sqlite3

# Initialize database
conn = sqlite3.connect('test.db')

print ("Opened database successfully");

# Create table function
def createtbl():
    conn.execute('''CREATE TABLE TEST
    (ID INTEGER PRIMARY KEY     NOT NULL,
     PURPOSE           TEXT    NOT NULL,
     NAME           TEXT    NOT NULL,
     WORD            TEXT     NOT NULL);''')
    print ("Table created successfully");

createtbl()
conn.close()
