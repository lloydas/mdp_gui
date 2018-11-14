import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

from global_def import *
from start_page import StartPage
from page_one import PageOne


class monitor(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.wm_title(self, "geostar")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames={}
		self.anis=[]

		for F in (StartPage, PageOne):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

			if F == PageOne:
				PageOne_g = frame.get_g()
				self.anis.append(PageOne_g)

		self.show_frame(StartPage)

	def get_ani(self):
		return self.anis

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


app = monitor()
anis = app.get_ani()
for g in anis:
	f = g.get_f()
	a = g.get_a()
	animation.FuncAnimation(f, animate(a), interval=100, repeat=True)
app.mainloop()




