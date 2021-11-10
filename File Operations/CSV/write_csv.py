#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pandas import DataFrame
import pandas as pd

order = pd.DataFrame({'OrderID': ['10251', '10252', '10253'],
                   'CustomerID': ['5', '1', '8'],
                   'OrderDate': ['11/02/2020', '11/02/2020', '11/02/2020']})
order.to_csv('newOrders.csv', index=False)