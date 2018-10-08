from tkinter import *
from tkinter import ttk
from frame import Frame
from button import button
import json


with open("values.json") as values_file:
	values_json = json.load(values_file)

root = Tk()

content = Frame(root, values_json["content"][0], values_json["content"][1])
frame = Frame(content.getObject(), values_json["frame"][0], values_json["frame"][1])
namelbl = ttk.Label(content.getObject(), text="Name")
button = button(frame.getObject(), values_json["button"][0], values_json["button"][1])

namelbl.grid(column=3, row=0, columnspan=2)


root.mainloop()

