#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        grid = Gtk.Grid()
        grid.set_column_spacing(15)
        self.add(grid)            
        
        combo = Gtk.ComboBoxText()
        grid.attach(combo, 0, 0, 1, 1)

        combo.connect("changed", self.on_changed)

        combo.append_text('Ubuntu')
        combo.append_text('Mandriva')
        combo.append_text('Redhat')
        combo.append_text('Gentoo')
        combo.append_text('Mint')
        
        self.label = Gtk.Label("")
        grid.attach(self.label, 1, 0, 1, 1)

        self.set_border_width(10)
        self.set_title("ComboBoxText")
        self.set_default_size(300, 220)
        self.connect("destroy", Gtk.main_quit)

    def on_changed(self, widget):
        self.label.set_label(widget.get_active_text())         

win = MyWindow()
win.show_all()
Gtk.main()