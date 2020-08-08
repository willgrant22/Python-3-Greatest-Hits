#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os, sys
from pathlib import Path

home = str(Path.home())
print(home)
os.mkdir(home+'/new', 0o777)
