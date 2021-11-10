#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import sqlite3
# Open db
conn = sqlite3.connect('test.db')
print ("Opened database successfully");
# Insert data
conn.execute("INSERT INTO TEST (PURPOSE,NAME,WORD) \
      VALUES ('purpose', 'name', 'word')");

conn.execute("INSERT INTO TEST (PURPOSE,NAME,WORD) \
      VALUES ('purpose2', 'name2', 'word2')");

conn.commit()
print ("Records created successfully");
conn.close()