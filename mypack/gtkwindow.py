#! /hint/python

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

from .appenditemquit import appendItemQuit

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gdk.set_program_class('Listador')
        Gtk.Window.__init__(self, title='言葉のリスト', application=app)
        self.set_size_request(220,70)
        self.set_resizable(False)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(1)

        self.entry_box_label = Gtk.Label(label='入力：')
        self.entry_box_label.set_halign(Gtk.Align.END)
        self.entry_box       = Gtk.Entry()
        self.entry_box.set_halign(Gtk.Align.START)

        self.grid.attach(self.entry_box_label, 0, 0, 1, 1)
        self.grid.attach(self.entry_box, 1, 0, 1, 1)

        self.quit_button = Gtk.Button()
        self.quit_button.set_label('完成')
        self.quit_button.set_halign(Gtk.Align.CENTER)
        self.quit_button.connect('clicked', self.callAppendItemQuit)
        self.grid.attach_next_to(self.quit_button, self.entry_box_label, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(self.grid)

    def callAppendItemQuit(self, entry_box):
        self.lista = self.entry_box.get_text().split(" ")
        appendItemQuit(self.lista)

class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = Window(self)
        win.show_all()

