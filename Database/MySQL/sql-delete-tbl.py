#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Delete table
# =============================================================================

import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database=""
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)