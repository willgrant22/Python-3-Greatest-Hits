#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

# Very simple table example
conn = sqlite3.connect('excel.db')
print ("Opened database successfully");
def createtbl():
    conn.execute('''CREATE TABLE TEST
    (ID INTEGER PRIMARY KEY     NOT NULL,
     SERVICE           TEXT    NOT NULL,
     USERNAME           TEXT    NOT NULL,
     PASSWORD            TEXT     NOT NULL);''')
    print ("Table created successfully");

createtbl()
conn.commit()
conn.close()
