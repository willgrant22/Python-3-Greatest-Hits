#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wx

# Import the widgets inspection tool
import wx.lib.inspection


class SizersSample(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Sizers sample')

        panel = wx.Panel(self)

        # Widgets creation
        radio_button = wx.RadioButton(panel, -1, "RadioButton")
        check_box = wx.CheckBox(panel, -1, "CheckBox")
        spin_ctrl = wx.SpinCtrl(panel, -1, "", min=0, max=100)
        text_ctrl_1 = wx.TextCtrl(panel, -1, "A first text control", style=wx.TE_MULTILINE)
        text_ctrl_2 = wx.TextCtrl(panel, -1, "A second text control", style=wx.TE_MULTILINE)

        # Starts of sizers section

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        center_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        static_text = wx.StaticText(panel, -1, "StaticText")
        main_sizer.Add(static_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        
        center_sizer.Add(radio_button, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer.Add(check_box, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer.Add(spin_ctrl, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

        main_sizer.Add(center_sizer, 0, wx.ALL|wx.EXPAND, 5)
        bottom_sizer.Add(text_ctrl_1, 1, wx.ALL|wx.EXPAND, 5)
        bottom_sizer.Add(text_ctrl_2, 1, wx.ALL|wx.EXPAND, 5)
        main_sizer.Add(bottom_sizer, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(main_sizer)

        main_sizer.Layout()
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()

    wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()
