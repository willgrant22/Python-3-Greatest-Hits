#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
# Background color
root.configure(background='gray')
root.title("Rotunda")

rot_i = Image.open("anap_logo.jpg")
rotunda = ImageTk.PhotoImage(rot_i)

label = tkinter.Label(image=rotunda)
label.image = rotunda
label.place(x=20, y=20)

root.mainloop()