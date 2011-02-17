#!/usr/bin/env python

# PyQrencode - Generate your own QrCode using 'qrencode'
#---------------------------------------------------------------------------------
# Qrencode Author : Kentaro Fukuchi
# PyQrencode Copyright (C) 2010 Suchakra <suchakra@fedoraproject.org> , <suchakra@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#---------------------------------------------------------------------------------

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import string
import sys
from subprocess import call
import webkit
import gobject


class PyQrDesktop(object):

	default_site = "/temp/QRcode" # Default location for webkit

	def on_window_main_destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("pyqr.glade")
		self.window_main = builder.get_object("window_main")
		builder.connect_signals(self)
	       	self.string = builder.get_object("string")
	       	self.pixels = builder.get_object("pix")
	       	self.margin = builder.get_object("mar")
	       	self.generate = builder.get_object("generate")
	       	self.web_view = builder.get_object("webkit")

# Start qrencode when 'Generate' is clicked. 
						
	def on_generate_clicked(self, widget):
		string_var = self.string.get_text()	
		pix_var = self.pixels.get_value()
		mar_var = self.margin.get_value()
		call(['qrencode', '-s', str(pix_var), '-m', str(mar_var), '-o', '/temp/QRcode', str(string_var)])
		self.web_view.open(self.default_site)
		print "Pixel:", pix_var
		print "Margin:", mar_var

if __name__ == "__main__":
	app = PyQrDesktop()
	app.window_main.show()
	gtk.main()
