#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from pathlib import Path
p = Path('.')
for name in p.glob('*.p*'):
    print(name)