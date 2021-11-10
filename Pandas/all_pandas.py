#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import pandas as pd

data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)


data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)


data = {'Name':['Tom', 'Jack', 'nick', 'juli'],
        'marks':[99, 98, 95, 90]}
df = pd.DataFrame(data, index =['rank1',
                                'rank2',
                                'rank3',
                                'rank4'])
print(df)


data = [{'a': 1, 'b': 2, 'c':3},
        {'a':10, 'b': 20, 'c': 30}]
df = pd.DataFrame(data)
print(df)


data = [{'b': 2, 'c':3}, {'a': 10, 'b': 20, 'c': 30}]
df = pd.DataFrame(data, index =['first', 'second'])
print(df)


Name = ['tom', 'krish', 'nick', 'juli']
Age = [25, 30, 26, 22]
list_of_tuples = list(zip(Name, Age))
df = pd.DataFrame(list_of_tuples,
                  columns = ['Name', 'Age'])
print(df)


d = {'one' : pd.Series([10, 20, 30, 40],
                       index =['a', 'b', 'c', 'd']),
      'two' : pd.Series([10, 20, 30, 40],
                        index =['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)