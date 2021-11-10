#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import tkinter

root = tkinter.Tk()
root.title('Centered window')

win_width = 300
win_height = 250 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Math to center window based on screen size
start_x = int((screen_width/2) - (win_width/2))
start_y = int((screen_height/2) - (win_height/2))

root.geometry('{}x{}+{}+{}'.format(win_width, win_height, 
    start_x, start_y))
root.mainloop()