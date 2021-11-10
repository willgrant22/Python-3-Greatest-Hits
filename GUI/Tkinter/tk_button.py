#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import tkinter

root = tkinter.Tk()
root.title('Quit button')

btn = tkinter.Button(root, text="Quit", width=8,
    command=root.quit)
btn.pack(pady=10)

root.geometry("300x250+300+300")
root.mainloop()