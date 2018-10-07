from tkinter import *
from tkinter import ttk
from frame import Frame

values = {"width": 200,
		  "height": 100,
		  "borderwidth": 5,
		  "relief": "solid"
		 }

root = Tk()


content = Frame(root)
frame = Frame(content.getObject(), values)
namelbl = ttk.Label(content.getObject(), text="Name")


content.render(column=0, row=0)
frame.render(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)


# content = ttk.Frame(root)
# frame = ttk.Frame(content, width=200, height=100)
# namelbl = ttk.Label(content, text="Name")


# content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)


root.mainloop()