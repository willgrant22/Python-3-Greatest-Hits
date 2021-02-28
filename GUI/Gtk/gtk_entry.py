#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        self.add(grid)        

        entry = Gtk.Entry()
        entry.connect("key-release-event", self.on_key_release)

        grid.attach(entry, 0, 0, 1, 1)

        self.label = Gtk.Label("")
        self.label.set_width_chars(15)

        grid.attach(self.label, 1, 0, 1, 1)

        self.set_border_width(5)

        self.set_title("Entry")
        self.set_default_size(300, 180)
        self.connect("destroy", Gtk.main_quit)

    def on_key_release(self, widget, event):
        self.label.set_text(widget.get_text())


win = MyWindow()
win.show_all()
Gtk.main()