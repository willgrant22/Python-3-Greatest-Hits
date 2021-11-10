#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Get and sort data descending
# =============================================================================

import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database=""
)


mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)