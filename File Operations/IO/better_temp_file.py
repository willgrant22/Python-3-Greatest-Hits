#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from tempfile import TemporaryFile

with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    data = fp.read()
    print(data)