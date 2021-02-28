#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wx
  
class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title, size = (500, 250)) 
             
      self.InitUI()
      self.Centre() 
      self.Show()      
         
   def InitUI(self): 
      panel = wx.Panel(self)
        
      hbox = wx.BoxSizer(wx.HORIZONTAL)
        
      fgs = wx.FlexGridSizer(3, 2, 10,10)
        
      title = wx.StaticText(panel, label = "Title: ") 
      author = wx.StaticText(panel, label = "Name of the Author: ") 
      review = wx.StaticText(panel, label = "Review: ")
        
      tc1 = wx.TextCtrl(panel) 
      tc2 = wx.TextCtrl(panel) 
      tc3 = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
        
      fgs.AddMany(
        [(title), (tc1, 1, wx.EXPAND),
         (author), (tc2, 1, wx.EXPAND), 
         (review), (tc3, 1, wx.EXPAND)]
         )  
      fgs.AddGrowableRow(2, 1) 
      fgs.AddGrowableCol(1, 1)  
      hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 20) 
      panel.SetSizer(hbox) 
        
app = wx.App() 
Example(None, title = 'FlexiGrid') 
app.MainLoop()