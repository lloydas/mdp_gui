from tkinter import Menu


class menuBar(Menu):
    def __init__(self, parent=None, values={}, position={}):
        self.menuBar = Menu(parent)

        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False

        self.values = values
        self.position = position

        # self.render()


    def addMenuFile(self, label, menuFile):
        self.menuBar.add_cascade(label=label, menu=menuFile)


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            self.menuBar.grid(column=self.position["column"])
        if "row" in self.position:
            self.menuBar.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.menuBar.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.menuBar.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.menuBar.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.menuBar.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.menuBar.grid(rowspan=self.position["rowspan"])
        self.menuBar.grid()


    def getObject(self):
        return self.menuBar


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def destroy(self):
        self.menuFile.destroy()



