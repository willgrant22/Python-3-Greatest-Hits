#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

a = ['foo', 'bar', 'baz']

itr = iter(a)
print(tuple(itr))


itr = iter(a)
print(set(itr))