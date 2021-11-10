#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wx 
 
app = wx.App() 
window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
window.Show(True)
 
app.MainLoop()