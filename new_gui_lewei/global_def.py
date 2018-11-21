import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import cv2

import tkinter as tk
from tkinter import ttk


def animate(a):
	img = cv2.imread('fig1.jpg', 0)
	a.hist(img.flatten(), normed=True, bins=30)


class GlobalVar(object):

	def __init__(self):
		self.f = Figure(figsize=(5,5), dpi=100)
		self.a = self.f.add_subplot(111)

	def get_f(self):
		return self.f

	def get_a(self):
		return self.a




