#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Get screen resolution
# =============================================================================
import wx

app = wx.App(False) # the wx.App object must be created first.    
print(wx.GetDisplaySize()) 