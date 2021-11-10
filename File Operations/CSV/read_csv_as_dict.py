#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import csv

orders = csv.DictReader(open("orders.csv"))
for order in orders:
    print(order['OrderID'])