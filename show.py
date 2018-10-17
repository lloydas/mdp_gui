from tkinter import *
from tkinter import ttk
from frame import frame
from button import button
from treeview import treeview
from menuBar import menuBar
from menuFile import menuFile
from label import label
from entry import entry
from text import text
from progressBar import progressBar
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
button1 = button(frame1, frame1.quit, values_json["button"][0], values_json["button"][1])
label = label(content.getObject(), values_json["label"][0], values_json["label"][1])
entry = entry(content.getObject(), values_json["entry"][0], values_json["entry"][1])
textBig = text(content.getObject(), values_json["textBig"][0], values_json["textBig"][1])
buttonPrintEntry = button(frame1, entry.getTextVal, values_json["buttonEntry"][0], values_json["buttonEntry"][1])
buttonPrintText = button(frame1, textBig.getTextVal, values_json["buttonText"][0], values_json["buttonText"][1])
progBar = progressBar(content.getObject(), values_json["progressBar"][0], values_json["progressBar"][1])
buttonProgBar = button(frame1, progBar.step, values_json["progButton"][0], values_json["progButton"][1])

menubar = menuBar(frame1, position=values_json["menubar"][0])
menuFile = menuFile(menubar.getObject())
menubar.addMenuFile("File", menuFile.getObject())


root.mainloop()

