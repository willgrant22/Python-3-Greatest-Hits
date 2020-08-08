#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Print directory and walk through sub-directories
# =============================================================================
# Imports
# =============================================================================
import glob, os
# Get current dir
cwd = os.getcwd()
# Initialize list
file_list = []
# Loop through dirs and get file list
for subdir, dirs, files in os.walk(cwd):
    for file in files:
        w = os.path.splitext(file)
        file_list.append(w)
# Print file list
for i in range(len(file_list)):
    print(file_list[i])