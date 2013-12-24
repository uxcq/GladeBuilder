#!/usr/bin/env python3.3
# -*- encoding: UTF-8 -*-

# 2013 Alexandre Vicenzi (vicenzi.alexandre at gmail com)

from datetime import datetime
from gi.repository import Gtk
from gladebuilder import GladeWindow

class MyWindow(GladeWindow):

	def __init__(self):
		GladeWindow.__init__(self, 'example-gtk3.glade', 'window1')

	def on_ok_clicked(self, *args):
		self.w.show({'entry1': 'Foo bar', 'button1': 'OK'})

	def on_close(self, *args):
		Gtk.main_quit(*args)

if __name__ == "__main__":
	Win = MyWindow()

	Win.w.scale1.set_range(0.0, 1)
	Win.w.scale2.set_range(0.0, 1)
	Win.w.spinbutton1.set_range(0.0, 1)


	distributions = ["Fedora", "Sabayon", "Debian", "Arch Linux", "Crunchbang"]
	liststore = Gtk.ListStore(str)
	for item in distributions:
		liststore.append([item])

	Win.w.comboboxtext1.set_model(liststore)

	cell = Gtk.CellRendererText()
	Win.w.combobox1.pack_start(cell, True)
	Win.w.combobox1.add_attribute(cell, "text", 0)
	Win.w.combobox1.set_model(liststore)

	dict = {
		"window1": "Example GTK 3",
		"button1": "Click",
		"togglebutton1": "Click me too",
		"checkbutton1": True,
		"entry1": "Some text",
		"spinbutton1": 0.2,
		"combobox1": 2,
		"comboboxtext1": 3,
		"label1": "<b>Bold label</b>",
		"linkbutton1": "https://www.google.com",
		"accellabel1": "<i>Italic accellabel</i>",
		"scalebutton1": 30,
		"volumebutton1": 0.8,
		"scale1": 0.5,
		"scale2": 0.6,
		"calendar1": datetime.today(),
		#"treeview1": ,
		#"treeview-selection1": ,
		#"textview1": ,
		"radiobutton1": False,
		"radiobutton2": True,
		"radiobutton3": True, # The last one wins.
		"spinner1": True,
		"progressbar1": 0.5,
	}

	Win.w.show(dict)

	dict = {
		"checkbutton1": "Is checked",
		'volumebutton1': 'Volume',
		'scalebutton1': 'Scale button',
		'linkbutton1': 'Go to google.com',
		'radiobutton1': 'First',
		'radiobutton2': 'Second',
		'radiobutton3': 'Third',
	}

	Win.w.show(dict)

	Win.show()