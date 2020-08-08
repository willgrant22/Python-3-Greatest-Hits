#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

i = 0
for i in range(100):
	i = i + 1
	file = open(f'testdir/file_{i}.txt', 'wb')
	file.write("whatever")
	file.close()