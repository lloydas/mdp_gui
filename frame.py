from tkinter import *
from tkinter import ttk


class Frame:
	def __init__(self, parent, values):
		self.state = dict()
		self.frameObject = ttk.Frame(parent)
		self.state["visible"] = False
		self.state["rendered"] = False
		self.values = values
		self.createWidgets()


	def createWidgets(self):
		for val in self.values:
			self.frameObject[val] = self.values[val]

	def getObject(self):
		return self.frameObject


	def setState(self, state):
		self.state = state


	def getState(self):
		return self.state


	def render(self, column=None, row=None, sticky=None, padx=None, pady=None, columnspan=None, rowspan=None):
		self.state["rendered"] = True
		self.state["visible"] = True
		if column is not None:
			self.frameObject.grid(column=column)
		if row is not None:
			self.frameObject.grid(row=row)
		if sticky is not None:
			self.frameObject.grid(sticky=sticky)
		if padx is not None:
			self.frameObject.grid(padx=padx)
		if pady is not None:
			self.frameObject.grid(pady=pady)
		if columnspan is not None:
			self.frameObject.grid(columnspan=columnspan)
		if rowspan is not None:
			self.frameObject.grid(rowspan=rowspan)
		self.frameObject.grid()


	def destroy(self):
		self.frameObject.destroy()








