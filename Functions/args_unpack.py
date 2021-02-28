#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

def func(name, age, location):
    print('name - ', name)
    print('age - ', age)
    print('location - ', location)


person = {"name":"will", "age":26, "location":"ohio"}

func(**person)