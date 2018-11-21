import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import os

import tkinter as tk
from tkinter import ttk

import page_one

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Start Page!!")

		self.tree = ttk.Treeview(self)
		files = os.listdir('data')
		id = self.tree.insert("", 'end', text="files")
		for f in files:
			first_child = self.tree.insert(id, 'end', text=f, tags=('onclick'))
			self.controller.add_frame(page_one.PageOne, f)
		self.tree.bind("<<TreeviewSelect>>", self.itemClicked, "+")

		# LAYOUT
		label.pack(pady=10, padx=10)
		self.tree.pack()

	def refresh(self):
		pass

	def itemClicked(self, arg):
		print("clicked")
		item = self.tree.focus()
		print('item',self.tree.item(item,"text"))
		if self.tree.item(item,"text") != "files":
			self.controller.show_frame(self.tree.item(item,"text"))



