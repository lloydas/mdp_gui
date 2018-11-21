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
        self.params = {"min": 0, "max": 255}

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(start_page.StartPage))
        button.pack()

        label_min = ttk.Label(self, text="min:")
        label_max = ttk.Label(self, text="max:")
        self.entry_min = ttk.Entry(self)        
        self.entry_max = ttk.Entry(self)        
        entry_button = ttk.Button(self, text="Update parameters", command=lambda: self.update())        

        # LAYOUT
        label_min.pack()
        self.entry_min.pack()
        label_max.pack()
        self.entry_max.pack()
        entry_button.pack()
        # label_min.grid(row=0, column=0, sticky=W)
        # label_min.grid(row=1, column=0, sticky=W)
        # self.entry_min.grid(row=0, column=1, columnspan=3, sticky=E)
        # self.entry_max.grid(row=0, column=1, columnspan=3, sticky=E)
        
        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update(self):
        self.params = {"min": int(self.entry_min.get()),
                       "max": int(self.entry_max.get())}
        self.refresh()

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number1 = 0
            return True

        try:
            self.entered_number1 = int(new_text)
            print(self.entered_number1)
            return True
        except ValueError:
            return False

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
                    normed=True)
        self.canvas.draw()



