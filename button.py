from tkinter import Button

class button(Button):
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def say_hi(self):
        print("hi there, everyone!")

    def createWidget(self):
        for i in self.values:
            self.b[i] = self.values[i]
        self.b["command"] = self.say_hi # this is an example for setting triggered function 
        self.b.pack(self.position) # might need to use render (grid) instead

    def __init__(self, parent=None, values={}, position={}):
        self.b = Button(parent)
        self.state = {"rendered": False,
                      "visible": True
                      }
        self.values = values
        self.position = position
        self.createWidget()


#render
#destroy, not sure whether button needs one

