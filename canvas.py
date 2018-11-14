from tkinter import Canvas, ALL
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class canvas(Canvas):
    def __init__(self, parent=None, values={}, position={}):
        self.object = Canvas(parent)
        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.canvas = None
        self.f = None
        self.render()
        self.createHist()


    def createHist(self):
        print('number of bins', self.values['n_bins'])
        N_points = self.values["N_points"]
        n_bins = self.values["n_bins"]
        x = np.random.randn(N_points)

        if self.f != None and self.canvas != None:
            print('clear canvas')
            self.f.clear()

        self.f = Figure(figsize=(self.values["figure_size_1"], self.values["figure_size_2"])) 
        p = self.f.gca()

        print('create f')

        p.hist(x, n_bins)
        p.set_xlabel('Median Value', fontsize = 15)
        p.set_ylabel('Frequency', fontsize = 15)
        canvas = FigureCanvasTkAgg(self.f, master=self.object)
        canvas.get_tk_widget().pack()
        print('draw canvas')
        canvas.draw()


    def set_values(self, values):
        self.values = values
        self.createHist()


    def get_values(self):
        return self.values


    def getObject(self):
        return self.object


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            print(self.position["column"])
            self.object.grid(column=self.position["column"])
        if "row" in self.position:
            self.object.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.object.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.object.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.object.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.object.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.object.grid(rowspan=self.position["rowspan"])
        self.object.grid()



    def destroy(self):
        self.object.destroy()


