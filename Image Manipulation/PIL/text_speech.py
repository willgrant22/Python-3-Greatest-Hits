#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from gtts import gTTS 
import os 

f = open("test.txt", "r")
for x in f:
	print(x)

language = 'en'

myobj = gTTS(text=x, lang=language, slow=False) 

myobj.save("welcome.mp3") 

os.system("mpg321 welcome.mp3") 

