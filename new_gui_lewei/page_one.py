import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import start_page
from global_def import *

g = GlobalVar()

class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		self.g = g

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One!!")
		label.pack(pady=10, padx=10)

		button = ttk.Button(self, text="Back to Home", command = lambda: controller.show_frame(start_page.StartPage))
		button.pack()		
		
		canvas = FigureCanvasTkAgg(g.get_f(), self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	def get_g(self):
		return self.g






