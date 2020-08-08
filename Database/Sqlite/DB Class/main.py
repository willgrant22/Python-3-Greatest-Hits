#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from db_class import createTBL, insertData, queryData
s = 'proton'
u = 'will.grant'
p = 'passtest'
ct = Database(s, u, p)
#ct.createTBL()
#ct.insertData()
ct.queryData()