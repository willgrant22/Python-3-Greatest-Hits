#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Created Date: 07/19/2018
# Description : Get list of processes for user
# =============================================================================
# Imports
# =============================================================================
import psutil

for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)