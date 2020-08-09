#!/usr/bin/env python3

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(355, 500))

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(14)

       	my_sizer = wx.BoxSizer(wx.VERTICAL)

       	my_sizer.Add((-1, 45))

       	st1 = wx.StaticText(panel, label='Line 1')
        st1.SetFont(font)
        my_sizer.Add(st1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=155)
        my_sizer.Add((-1, 5))

        self.text_ctrl1 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55) 
        my_sizer.Add((-1, 10))

        st2 = wx.StaticText(panel, label='Line 2')
        st2.SetFont(font)
        my_sizer.Add(st2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=155)
        my_sizer.Add((-1, 5))

        self.text_ctrl2 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55) 
        my_sizer.Add((-1, 10))

        st3 = wx.StaticText(panel, label='Line 3')
        st3.SetFont(font)
        my_sizer.Add(st3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=155)
        my_sizer.Add((-1, 5))

        self.text_ctrl3 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55) 
        my_sizer.Add((-1, 10))

        st4 = wx.StaticText(panel, label='Line 4')
        st4.SetFont(font)
        my_sizer.Add(st4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=155)
        my_sizer.Add((-1, 5))

        self.text_ctrl4 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55) 
        my_sizer.Add((-1, 10))

        st5 = wx.StaticText(panel, label='Line 5')
        st5.SetFont(font)
        my_sizer.Add(st5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=155)
        my_sizer.Add((-1, 5))

        self.text_ctrl5 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55) 
        my_sizer.Add((-1, 45))

        my_btn = wx.Button(panel, label='Submit')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55)
        my_sizer.Add((-1,10))

        my_btn2 = wx.Button(panel, label='Clear All')
        my_btn2.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn2, 0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=55)

        panel.SetSizer(my_sizer)

        self.Show()

        self.Centre()


    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')


def main():

    app = wx.App()
    ex = Example(None, title='Vertical Form')
    ex.Show()
    app.MainLoop()


main()