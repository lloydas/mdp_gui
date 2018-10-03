'''
This is an informal test for button.py
New test would be written for all classes after the new Frame class is finished.

Lewei
'''
from tkinter import *
from button import button


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        # self.QUIT = Button(self)
        # self.QUIT["text"] = "QUIT"
        # self.QUIT["fg"]   = "red"
        # self.QUIT["command"] =  self.quit

        # self.QUIT.pack({"side": "left"})

        # self.hi_there = Button(self)
        # self.hi_there["text"] = "Hello",
        # self.hi_there["command"] = self.say_hi

        # self.hi_there.pack({"side": "left"})
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

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
# root.destroy()


