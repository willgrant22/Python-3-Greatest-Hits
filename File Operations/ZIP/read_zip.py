#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    print(zipobj.namelist())