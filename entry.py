from tkinter import *
from tkinter import ttk

class entry():
    def __init__(self, parent=None, values={}, canvas=None):
        self.text = StringVar()
        self.object = ttk.Entry(parent, textvariable=self.text)
        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False
        self.values = values
        # self.position = position
        self.createWidgets()
        # self.render()
        self.canvas = canvas


    def createWidgets(self):
        for val in self.values:
            self.object[val] = self.values[val]
        if "textvariable" in self.values:
        	self.object.insert(0, self.values["textvariable"])


    def getTextVal(self):
        print('entry value for canvas', self.object.get())
        v_canvas = self.canvas.get_values()
        v_canvas["n_bins"] = int(self.object.get())
        self.canvas.set_values(v_canvas)
        return self.object.get()
        # set the canvas from the entry value


    def getObject(self):
        return self.object


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def render(self, position):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in position:
            self.object.grid(column=position["column"])
        if "row" in position:
            self.object.grid(row=position["row"])
        if "sticky" in position:
            self.object.grid(sticky=position["sticky"])
        if "padx" in position:
            self.object.grid(padx=position["padx"])
        if "pady" in position:
            self.object.grid(pady=position["pady"])
        if "columnspan" in position:
            self.object.grid(columnspan=position["columnspan"])
        if "rowspan" in position:
            self.object.grid(rowspan=position["rowspan"])
        self.object.grid()


    def destroy(self):
        self.object.destroy()


