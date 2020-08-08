//#!/usr/bin/env python3
//# -*- coding: utf-8 -*-
//# =============================================================================
//# Author :  Will Grant
//# =============================================================================

#include <stdio.h>

void myprint(void);

void myprint()
{
    printf("hello world\n");
}
//gcc -shared -Wl,-install_name,testlib.so -o testlib.so -fPIC testlib.c
