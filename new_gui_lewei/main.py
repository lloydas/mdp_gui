import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import sys

import tkinter as tk
from tkinter import ttk

from global_def import *
from start_page import StartPage
from page_one import PageOne


class monitor(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "geostar")

        self.dirname = args[0]
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames={}

        # Display Start Page
        frame = StartPage(self.container, self, self.dirname)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, filename):
        frame = self.frames[filename]
        frame.tkraise()
        frame.refresh()

    def add_frame(self, cont, filename, h5_status=False, img=None, raster=None):
        frame = cont(self.container, self, filename, h5_status, img, raster)
        self.frames[filename] = frame
        frame.grid(row=0, column=0, sticky="nsew")


def main():
    dirname = sys.argv[1]
    app = monitor(dirname)
    app.mainloop()


if __name__ == "__main__":
    main()



