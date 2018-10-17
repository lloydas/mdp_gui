from tkinter import *
from tkinter import ttk
from frame import frame
from button import button
from treeview import treeview
from menuBar import menuBar
from menuFile import menuFile
from label import label
import json


with open("values.json") as values_file:
	values_json = json.load(values_file)

root = Tk()

content = frame(root, values_json["content"][0], values_json["content"][1])
tree = treeview(content.getObject())
tree.addFile("a1.h5")
tree.addFile("a1.h5")
frame = frame(content.getObject(), values_json["frame"][0], values_json["frame"][1])
frame1 = frame.getObject()
button = button(frame1, frame1.quit, values_json["button"][0], values_json["button"][1])
label = label(content.getObject(), values_json["label"][0], values_json["label"][1])
# menubar = menuBar(frame.getObject(), values_json["menubar"][0])


root.mainloop()

