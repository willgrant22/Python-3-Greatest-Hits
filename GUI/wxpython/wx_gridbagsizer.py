#!/usr/bin/env python3

import wx  

class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title, size = (450,300)) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()      
         
   def InitUI(self):

      menubar = wx.MenuBar() 
        
      fileMenu = wx.Menu() 
      newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "New",kind = wx.ITEM_NORMAL) 
       
      fileMenu.AppendItem(newitem) 
        
      fileMenu.AppendSeparator()
        
      editMenu = wx.Menu() 
      copyItem = wx.MenuItem(editMenu, 100,text = "copy",kind = wx.ITEM_NORMAL)
       
        
      editMenu.AppendItem(copyItem) 
      cutItem = wx.MenuItem(editMenu, 101,text = "cut",kind = wx.ITEM_NORMAL) 
      
        
      editMenu.AppendItem(cutItem) 
      pasteItem = wx.MenuItem(editMenu, 102,text = "paste",kind = wx.ITEM_NORMAL) 
      
        
      editMenu.AppendItem(pasteItem) 
      fileMenu.AppendMenu(wx.ID_ANY, "Edit", editMenu) 
      fileMenu.AppendSeparator() 
         
      radio1 = wx.MenuItem(fileMenu, 200,text = "Radio1",kind = wx.ITEM_RADIO) 
      radio2 = wx.MenuItem(fileMenu, 300,text = "radio2",kind = wx.ITEM_RADIO) 
        
      fileMenu.AppendItem(radio1) 
      fileMenu.AppendItem(radio2) 
      fileMenu.AppendSeparator() 
         
      fileMenu.AppendCheckItem(103,"Checkable") 
      quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        
      fileMenu.AppendItem(quit) 
      menubar.Append(fileMenu, '&File') 
        
      self.SetMenuBar(menubar) 
       
      panel = wx.Panel(self) 
      sizer = wx.GridBagSizer(0,0)


      sizer.Add((15, 15), (0, 0))
      sizer.Add((15, 15), (0, 1))
        
      text = wx.StaticText(panel, label = " Name: ") 
      sizer.Add(text, pos = (1, 0), flag = wx.ALL, border = 5)
        
      tc = wx.TextCtrl(panel) 
      sizer.Add(tc, pos = (1, 1), span = (-1, 4), flag = wx.EXPAND|wx.ALL, border = 5) 
         
      text1 = wx.StaticText(panel, label = " Address: ") 
      sizer.Add(text1, pos = (2, 0), flag = wx.ALL, border = 5) 
        
      tc1 = wx.TextCtrl(panel) 
      sizer.Add(tc1, pos = (2,1), span = (-1, 4), flag = wx.EXPAND|wx.ALL, border = 5) 
         
      text2 = wx.StaticText(panel,label = " Age: ") 
      sizer.Add(text2, pos = (3, 0), flag = wx.ALL, border = 5) 
        
      tc2 = wx.TextCtrl(panel) 
      sizer.Add(tc2, pos = (3,1), flag = wx.ALL, border = 5) 
        
      text3 = wx.StaticText(panel,label = "Mob.No: ") 
      sizer.Add(text3, pos = (3, 2), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
        
      tc3 = wx.TextCtrl(panel) 
      sizer.Add(tc3, pos = (3,3), flag = wx.ALL, border = 5) 
         
      text4 = wx.StaticText(panel, label = " Description: ") 
      sizer.Add(text4, pos = (4, 0), flag = wx.ALL, border = 5) 
        
      tc4 = wx.TextCtrl(panel,style =  wx.TE_MULTILINE) 
      sizer.Add(tc4, pos = (4,1), span = (0,4), flag = wx.EXPAND|wx.ALL, border = 5) 
      sizer.AddGrowableRow(4) 
         
      buttonOk = wx.Button(panel, label = "Ok")
      buttonClose = wx.Button(panel, label = "Close" ) 
        
      sizer.Add(buttonOk, pos = (5, 2),flag = wx.ALL, border = 10) 
      sizer.Add(buttonClose, pos = (5, 3), flag = wx.ALL, border = 10)

      sizer.Add((15, 15), (6, 0))
        
      panel.SetSizerAndFit(sizer)
        
app = wx.App() 
Example(None, title = 'GridBag Demo') 
app.MainLoop()