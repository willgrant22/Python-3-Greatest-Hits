#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from functools import wraps

def add_last(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs) + ' grant'
    return wrapper

@add_last
def will():
    return 'will'

print(will())