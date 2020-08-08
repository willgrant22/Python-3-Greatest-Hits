
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

with open('words.txt', 'r') as f:

    while line := f.readline():

        print(line.rstrip())