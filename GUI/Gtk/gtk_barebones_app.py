#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        super(Window, self).__init__(title="Application", application=app)

        grid = Gtk.Grid()

        menubar = Gtk.MenuBar()

        fmi = Gtk.MenuItem.new_with_label("File")

        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("Exit") 
        emi.connect("activate", self.quitApp)
        menu.append(emi)
             
        fmi.set_submenu(menu)

        menubar.add(fmi)

        grid.attach(menubar, 0, 0, 1, 1)

        self.add(grid)

        self.set_default_size(280, 180)

    def quitApp(self, par):

        app.quit()
   

class Application(Gtk.Application):

    def __init__(self):
        super(Application, self).__init__()

    def do_activate(self):
    
        self.win = Window(self)
        self.win.show_all()

    def do_startup(self):

        Gtk.Application.do_startup(self)

app = Application()
app.run(sys.argv)