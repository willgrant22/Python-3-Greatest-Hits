#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from db_class import *

s = 'proton'
u = 'will.grant.22'
p = 'passtest'

ct = Database(s, u, p)
# Other functions that can be called
#ct.createTBL()
#ct.insertData()
ct.queryData()