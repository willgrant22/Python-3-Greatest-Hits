#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

from mailsql import Database, InsertData, CreateTbl

@InsertData
def insert_it(**kwargs):
	return kwargs

@CreateTbl
def table_it(**kwargs):
	return kwargs

@Database
def create_it(**kwargs):
	return kwargs





