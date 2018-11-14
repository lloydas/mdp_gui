import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import page_one
from global_def import *

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page!!")
		label.pack(pady=10, padx=10)

		button = ttk.Button(self, text="Visit Page 1", command = lambda: controller.show_frame(page_one.PageOne))
		button.pack()



