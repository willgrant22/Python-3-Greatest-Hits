#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import csv
with open('orders.csv', 'w', newline='') as file:
    fieldnames = ['OrderID', 'CustomerID', 'OrderDate']
    order = csv.DictWriter(file, fieldnames=fieldnames)
    order.writeheader()
    order.writerow({'OrderID': '10251', 'CustomerID': 7, 'OrderDate': '11/02/2020'})
    order.writerow({'OrderID': '10252', 'CustomerID': 3, 'OrderDate': '11/02/2020'})
    order.writerow({'OrderID': '10253', 'CustomerID': 1, 'OrderDate': '11/02/2020'})