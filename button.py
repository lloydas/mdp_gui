from tkinter import Button


class button(Button):
    def __init__(self, parent=None, func=None, values={}, position={}):
        self.buttonObject = Button(parent)
        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.func = func
        self.createWidgets()


    def createWidgets(self):
        for val in self.values:
            self.buttonObject[val] = self.values[val]
        self.buttonObject["command"] = self.func
        self.buttonObject.pack(self.position) # might need to use render (grid) instead


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def destroy(self):
        self.buttonObject.destroy()


#render
#destroy, not sure whether button needs one

