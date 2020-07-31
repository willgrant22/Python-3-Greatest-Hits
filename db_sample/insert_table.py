#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("INSERT INTO COMMANDS (ID,PURPOSE,TESTCMD,UBUNTUCMD) \
      VALUES (1, 'Update', 'ast-sys -u', 'sudo apt update'  )");

conn.execute("INSERT INTO COMMANDS (ID,PURPOSE,TESTCMD,UBUNTUCMD) \
      VALUES (2, 'Upgrade', 'ast-sys -uG', 'sudo apt upgrade -y' )");

conn.execute("INSERT INTO COMMANDS (ID,PURPOSE,TESTCMD,UBUNTUCMD) \
      VALUES (3, 'Autoclean', 'ast-sys -aC', 'sudo apt autoclean -y' )");

conn.execute("INSERT INTO COMMANDS (ID,PURPOSE,TESTCMD,UBUNTUCMD) \
      VALUES (4, 'Reboot', 'ast-sys -r', 'reboot' )");


conn.commit()
print ("Records created successfully");
conn.close()