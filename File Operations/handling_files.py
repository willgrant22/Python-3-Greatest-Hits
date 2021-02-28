#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import os
import shutil

print("The current directory:", os.getcwd())

os.mkdir("folder")
os.chdir("folder")

print("The current directory changing the directory to folder:", os.getcwd())

os.chdir("..")
os.makedirs("nested1/nested2/nested3")

text_file = open("text.txt", "w")
text_file.write("This is a text file")

os.rename("text.txt", "renamed-text.txt")
os.replace("renamed-text.txt", "folder/renamed-text.txt")

print("All folders & files:", os.listdir())


for dirpath, dirnames, filenames in os.walk("."):
    for dirname in dirnames:
        print("Directory:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("File:", os.path.join(dirpath, filename))
os.remove("folder/renamed-text.txt")
os.rmdir("folder")
os.removedirs("nested1/nested2/nested3")

shutil.rmtree("nested1")

open("text.txt", "w").write("This is a text file")

print(os.stat("text.txt"))

print("File size:", os.stat("text.txt").st_size)
