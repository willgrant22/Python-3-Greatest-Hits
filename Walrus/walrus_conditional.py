
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

words = ['falcon', 'sky', 'ab', 'water', 'a', 'b', 'forest']

for word in words:
    if ((n := len(word)) < 3):
        print(f'warning, the word {word} has {n} characters')