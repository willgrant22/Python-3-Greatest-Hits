import wx



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size= (600,400))




        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)



        gridSizer = wx.GridSizer(4,4,5,5)

        for i in range(1,17):
            btn = "Btn" + str(i)

            gridSizer.Add(wx.Button(self, label = btn),0,wx.EXPAND )



        self.SetSizer(gridSizer)





class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid Sizer")
        self.frame.Show()
        return True



app = MyApp()
app.MainLoop()