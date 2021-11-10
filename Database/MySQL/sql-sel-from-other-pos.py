#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Offset data
# =============================================================================

import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database=""
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)