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
        self.render()


    def createWidgets(self):
        for val in self.values:
            self.buttonObject[val] = self.values[val]
        self.buttonObject["command"] = self.func


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            print(self.position["column"])
            self.buttonObject.grid(column=self.position["column"])
        if "row" in self.position:
            self.buttonObject.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.buttonObject.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.buttonObject.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.buttonObject.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.buttonObject.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.buttonObject.grid(rowspan=self.position["rowspan"])
        self.buttonObject.grid()


    def destroy(self):
        self.buttonObject.destroy()


#render
#destroy, not sure whether button needs one

