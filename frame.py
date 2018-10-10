from tkinter import *
from tkinter import ttk


class Frame:
    def __init__(self, parent=None, values={}, position={}):
        self.frameObject = ttk.Frame(parent, style='r.TFrame')
        self.state = dict()     
        self.state["visible"] = False
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.createWidgets()
        self.render()


    def createWidgets(self):
        if self.values is not None:
            for val in self.values:
                self.frameObject[val] = self.values[val]


    def getObject(self):
        return self.frameObject


    def setState(self, state):
        self.state = state


    def getState(self):
        return self.state


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            self.frameObject.grid(column=self.position["column"])
        if "row" in self.position:
            self.frameObject.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.frameObject.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.frameObject.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.frameObject.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.frameObject.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.frameObject.grid(rowspan=self.position["rowspan"])
        self.frameObject.grid()


    def destroy(self):
        self.frameObject.destroy()

