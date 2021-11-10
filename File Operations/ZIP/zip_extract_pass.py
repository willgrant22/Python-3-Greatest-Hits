#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import zipfile

with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
    # Extract from a password protected archive
    pwd_zip.extractall(path='extract_dir', pwd='')