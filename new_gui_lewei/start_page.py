import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from PIL import ImageTk,Image
import os
import pandas as pd
import numpy as np
import h5py

import tkinter as tk
from tkinter import ttk

import page_one

class StartPage(tk.Frame):

    def __init__(self, parent, controller, dirname):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.dirname = dirname
        self.curr_file = None
        self.curr_photo = None
        self.curr_h5_status = False

        label = tk.Label(self, text="Start Page!!")
        button = ttk.Button(self, text="Info of image raster", command=lambda: self.itemInfo())

        self.tree = ttk.Treeview(self)
        files = os.listdir(self.dirname)
        id = self.tree.insert("", 'end', text=self.dirname)
        for f in files:
            f_path = os.path.join(self.dirname, f)
            if f == ".DS_Store" or os.path.isdir(f_path):
                continue
            if f.split('.')[-1] == "h5":
                curr_child = self.tree.insert(id, 'end', text=f)
                h5_file = h5py.File(f_path, 'r')
                h5_imgs = list(h5_file.keys())
                for h5_img in h5_imgs:
                    h5_child = self.tree.insert(curr_child, 'end', text=h5_img)
                    f_img_data = h5_file[h5_img]
                    f_img_rasters = list(k for k in f_img_data.keys())
                    for raster in f_img_rasters:
                        ras_child = self.tree.insert(h5_child, 'end', text=raster, tags=('h5'))
                        self.controller.add_frame(page_one.PageOne, f_path, True, h5_img, raster)
            elif f.split('.')[-1] != "":
                curr_child = self.tree.insert(id, 'end', text=f, tags=('non-h5'))
                self.controller.add_frame(page_one.PageOne, f_path)
        self.tree.tag_bind('non-h5', '<ButtonRelease>', self.nonh5Clicked)
        self.tree.tag_bind('h5', '<ButtonRelease>', self.h5Clicked)

        # LAYOUT
        label.pack(pady=10, padx=10)
        self.tree.pack()
        button.pack()

        self.canvas = tk.Canvas(self, width = 300, height = 300)
        self.canvas.pack()
        # self.canvas = FigureCanvasTkAgg(self.f, self)
        # self.canvas.draw()
        # self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def refresh(self):
        self.canvas.create_image(20, 20, anchor=tk.NW, image=self.curr_photo)

    def h5Clicked(self, arg):
        raster = self.tree.focus()
        raster_name = self.tree.item(raster,"text")
        img = self.tree.parent(raster)
        img_name = self.tree.item(img,"text")
        h5file = self.tree.parent(img)
        h5_name = self.tree.item(h5file, "text")
        self.curr_file = os.path.join(self.dirname, h5_name)
        print("clicked on", self.curr_file)

        h5_data = h5py.File(self.curr_file, 'r')
        img_data = h5_data[img_name]
        raster_data = img_data[raster_name].value
        display_data = Image.fromarray(raster_data)
        display_data = display_data.resize((300, 300))
        # obtain image data for display

        self.curr_h5_status = True
        self.img = img_name
        self.raster = raster_name
        self.curr_photo = ImageTk.PhotoImage(display_data)
        self.canvas.create_image(20, 20, anchor=tk.NW, image=self.curr_photo)

    def nonh5Clicked(self, arg):
        item = self.tree.focus()
        item_name = self.tree.item(item,"text")
        self.curr_file = os.path.join(self.dirname, item_name)
        print("clicked on", self.curr_file)

        display_data = Image.open(self.curr_file)
        display_data = display_data.resize((300, 300))
        # obtain image data for display

        self.curr_photo = ImageTk.PhotoImage(display_data)
        self.canvas.create_image(20, 20, anchor=tk.NW, image=self.curr_photo)

    def itemInfo(self):
        if self.curr_file is None:
            print("Choose an item to display info")
        elif self.curr_h5_status == False:
            self.controller.show_frame(self.curr_file)
        else:
            self.controller.show_frame(self.curr_file)


