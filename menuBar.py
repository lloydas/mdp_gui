from tkinter import Menu


class menuBar(Menu):
    def __init__(self, parent=None, values={}, position={}):
        self.menuBar = Menu(parent)

        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False

        self.values = values
        self.position = position

        self.createWidgets()

        # values: {
        #     'menufiles':{
        #         'Label1': menuFile
        #     }
        # }


    def createWidgets(self):
        for label in self.values['menufiles']:
            self.menuBar.add_cascade(label=label, menu=self.values['menufiles'][label])
            # self.buttonObject.pack(self.position) # might need to use render (grid) instead


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def destroy(self):
        self.menuFile.destroy()



