#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Create MySQL table
# =============================================================================
import mysql.connector

mydb = mysql.connector.connect(
  host="", 	# DB ip address
  user="", 	# DB user
  passwd="" # DB password
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE TEST")