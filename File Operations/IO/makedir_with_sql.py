#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3
import os, sys
from pathlib import Path
home = str(Path.home())
print(home)
os.makedirs(home+'/new/db/', 0o777)

conn = sqlite3.connect(home+'/new/db/'+'ast69.db')
print ("Opened database successfully");
def createtbl():
    conn.execute('''CREATE TABLE COMMANDS
    (ID INT PRIMARY KEY     NOT NULL,
     PURPOSE           TEXT    NOT NULL,
     TESTCMD           TEXT    NOT NULL,
     UBUNTUCMD            TEXT     NOT NULL);''')
    print ("Table created successfully");

createtbl()
conn.close()
