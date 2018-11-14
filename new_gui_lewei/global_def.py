import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk


def animate(a):
	data = open("try.txt", "r").readlines()
	xlist = []
	ylist = []
	for d in data:
		if len(d) > 1:
			x, y = d.split(",")
			xlist.append(int(x))
			ylist.append(int(y))
	a.clear()
	a.plot(xlist, ylist)


class GlobalVar(object):

	def __init__(self):
		self.f = Figure(figsize=(5,5), dpi=100)
		self.a = self.f.add_subplot(111)

	def get_f(self):
		return self.f

	def get_a(self):
		return self.a




