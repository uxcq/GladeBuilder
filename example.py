#!/usr/bin/env python3.3
# -*- encoding: UTF-8 -*-

# 2013 Alexandre Vicenzi (vicenzi.alexandre at gmail com)

from gi.repository import Gtk
from gladewindow import GladeWindow

class MyWindow(GladeWindow):

	def __init__(self):
		GladeWindow.__init__(self, 'win.glade', 'window1')

	def on_ok_clicked(self, *args):
		self.w.show({'entry1': 'Foo bar', 'button1': 'OK'})

	def on_close(self, *args):
		Gtk.main_quit(*args)

if __name__ == "__main__":
	Win = MyWindow()
	Win.w.show({'window1': 'Example', 'label1': 'Name:', 'entry1': 'Alexandre Vicenzi', 'button1': 'Click-me'})
	Win.show()