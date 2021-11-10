#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

print(full_name('will', 'grant'))

add_one = lambda x: x + 1

print(add_one(2))

print((lambda x, y: x + y)(2, 3))


high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))

def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'