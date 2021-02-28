#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

adder = lambda x, y: x + y
print (adder (1, 2))

double = lambda x: x * 2

# Output: 10
print(double(5))

my_list1 = [1, 5, 4, 6, 8, 11, 3, 12]

new_list1 = list(filter(lambda x: (x%2 == 0) , my_list1))

# Output: [4, 6, 8, 12]
print(new_list1)

my_list2 = [1, 5, 4, 6, 8, 11, 3, 12]

new_list2 = list(map(lambda x: x * 2 , my_list2))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list2)