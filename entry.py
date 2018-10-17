from tkinter import *
from tkinter import ttk

class entry():
    def __init__(self, parent=None, values={}, position={}):
        self.text = StringVar()
        self.object = ttk.Entry(parent, textvariable=self.text)
        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.createWidgets()
        self.render()


    def createWidgets(self):
        for val in self.values:
            self.object[val] = self.values[val]
        if "textvariable" in self.values:
        	self.object.insert(0, self.values["textvariable"])



    def getTextVal(self):
    	print(self.object.get())


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


