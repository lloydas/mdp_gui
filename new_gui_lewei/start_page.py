import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from PIL import ImageTk,Image 
import os
import cv2

import tkinter as tk
from tkinter import ttk

import page_one

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.curr_img = None
		label = tk.Label(self, text="Start Page!!")
		button = ttk.Button(self, text="Info of image", command=lambda: self.itemInfo())

		self.tree = ttk.Treeview(self)
		files = os.listdir('data')
		id = self.tree.insert("", 'end', text="files")
		for f in files:
			if f == ".DS_Store":
				continue
			first_child = self.tree.insert(id, 'end', text=f, tags=('onclick'))
			self.controller.add_frame(page_one.PageOne, f)
		self.tree.bind("<<TreeviewSelect>>", self.itemClicked, "+")

		# LAYOUT
		label.pack(pady=10, padx=10)
		self.tree.pack()
		button.pack()

		self.canvas = tk.Canvas(self, width = 300, height = 300)
		self.canvas.pack()
		# self.canvas = FigureCanvasTkAgg(self.f, self)
  #       self.canvas.draw()
  #       self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
  #       self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	def refresh(self):
		pass

	def itemClicked(self, arg):
		print("clicked")
		item = self.tree.focus()
		print('item',self.tree.item(item,"text"))
		if self.tree.item(item,"text") != "files":
			self.curr_img = self.tree.item(item,"text")
			img = ImageTk.PhotoImage(Image.open("data/" + self.curr_img))  
			self.canvas.create_image(20, 20, anchor=tk.NW, image=img)
			self.canvas.show()

	def itemInfo(self):
		print("info")
		if self.curr_img is not None:
			self.controller.show_frame(self.curr_img)



