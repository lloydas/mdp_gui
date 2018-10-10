from tkinter import Menu


class menuFile(Menu):
    def __init__(self, parent=None, values={}, position={}):
        self.menuFile = Menu(parent)

        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False

        self.values = values
        self.position = position

        self.createWidgets()

        # values: {
        #     'label': 'Label1',
        #     'command': {
        #         'New': func_new,
        #         'Open': func_open
        #     }
        # }


    def createWidgets(self):
        for cmd in self.values['command']:
            self.menuFile.add_command(label=cmd, command=self.newfile)
            # self.menuFile.add_command(label=cmd, command=self.values['command'][cmd])


    def newfile(self):
        print("new file")


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def destroy(self):
        self.menuFile.destroy()



