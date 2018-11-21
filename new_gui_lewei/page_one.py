import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import cv2

import tkinter as tk
from tkinter import ttk, W, E

import start_page


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        self.f = Figure(figsize=(5,5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.img = None
        self.params = {"min": 0, "max": 255, "bins": 10}

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!")
        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(start_page.StartPage))        

        label_min = ttk.Label(self, text="min:")
        label_max = ttk.Label(self, text="max:")
        label_bins = ttk.Label(self, text="number of bins:")
        self.entry_min = ttk.Entry(self)        
        self.entry_max = ttk.Entry(self)
        self.entry_bins = ttk.Entry(self)
        self.entry_min.insert(0, "0")
        self.entry_max.insert(0, "255")
        self.entry_bins.insert(0, "10")
        entry_button = ttk.Button(self, text="Update parameters", command=lambda: self.update())        
        
        # LAYOUT
        label.pack(pady=10, padx=10)
        button.pack()
        label_min.pack()
        self.entry_min.pack()
        label_max.pack()
        self.entry_max.pack()
        label_bins.pack()
        self.entry_bins.pack()
        entry_button.pack()
        # label_min.grid(row=0, column=0, sticky=W)
        # label_min.grid(row=1, column=0, sticky=W)
        # self.entry_min.grid(row=0, column=1, columnspan=3, sticky=E)
        # self.entry_max.grid(row=0, column=1, columnspan=3, sticky=E)

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()

    def update(self):
        self.params = {"min": int(self.entry_min.get()),
                       "max": int(self.entry_max.get()),
                       "bins": int(self.entry_bins.get()),}
        self.refresh()

    def refresh(self):
        print('refresh')
        print('params', self.params)
        if self.img is None:
            self.img = cv2.imread('fig1.jpg', 0)
        self.animate()

    def animate(self):
        self.a.clear()
        self.a.hist(self.img.flatten(),
                    range=(self.params["min"], self.params["max"]),
                    bins=self.params["bins"],
                    normed=True)
        self.canvas.draw()



