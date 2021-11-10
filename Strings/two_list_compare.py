#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pandas import DataFrame
import pandas as pd

def compare_two_lists() -> bool:
   
    list1 = [
        {'id': '123-abc', 'name': 'Mike', 'age': 40},
        {'id': '123-efg', 'name': 'John', 'age': 24},
        {'id': '123-xyz', 'name': 'Aly', 'age': 35}
    ]

    list2 = [
        {'id': '123-abc', 'name': 'Mike', 'age': 40},
        {'id': '123-efg', 'name': 'Jon', 'age': 24},
        {'id': '123-xyz', 'name': 'Aly', 'age': 32}
    ]
    
    df1 = pd.DataFrame(list1)
    df2 = pd.DataFrame(list2)
    diff = dataframe_difference(df1, df2)
    result = len(diff) == 0
    if not result:
        print(f'There are {len(diff)} differences:\n{diff.head()}')
    return result

def dataframe_difference(df1: DataFrame, df2: DataFrame) -> DataFrame:
    
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    diff_df = comparison_df[comparison_df['_merge'] != 'both']
    print(df1)
    return diff_df
compare_two_lists()