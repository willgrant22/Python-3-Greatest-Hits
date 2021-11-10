#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import subprocess
import sys

infile = "final.txt"
outfile = "cleaned_final.txt"

delete_list = ['\033[1;94m', '\033[1;91m', '\033[1;97m', '\033[1;93m', '\033[1;35m', '\033[1;32m','\033[1;36m', '\033[0m']
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

test = subprocess.Popen(["open", f'{outfile}'], stdout=subprocess.PIPE)
output = test.communicate()[0]