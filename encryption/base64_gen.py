#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import random
key = ''.join(chr(random.randint(0, 0xFF)) for i in range(256))
print('key', [x for x in key])

iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(256)])
print('key', [x for x in iv])
