#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wx

def onButton(event):
    print ("Button pressed.")

app = wx.App()

frame = wx.Frame(None, -1, 'win.py')
frame.SetSize(0,0,200,50)

# Create open file dialog
openFileDialog = wx.FileDialog(frame, "Open", "", "", 
      "Python files (*.py)|*.py", 
       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

openFileDialog.ShowModal()
print(openFileDialog.GetPath())
openFileDialog.Destroy()