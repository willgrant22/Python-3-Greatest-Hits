#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3 as lite
from prettytable import from_db_cursor

con = lite.connect('data.db')
    
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT * FROM Cities')   
    
    x = from_db_cursor(cur) 
    
print(x)