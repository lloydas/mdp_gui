'''
This is an informal test for button.py
New test would be written for all classes after the new Frame class is finished.

Lewei
'''
from tkinter import *
from button import button
from frame import frame


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.createWidgets()


    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        values = {
        "text": "say_hi",
        "fg": "red",
        "relief": SUNKEN,
        "disabledforeground": "blue"
        }
        position = {"side": "left"}
        self.hi = button(parent=self,
                         values=values, 
                         position=position)


root = Tk()
app = Application(master=root)
app.mainloop()
# root.destroy()


