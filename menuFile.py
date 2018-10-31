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


    def createWidgets(self):
        self.menuFile.add_command(label='New', command=self.newfile)
        self.menuFile.add_command(label='Open...', command=self.openfile)
        self.menuFile.add_command(label='Close', command=self.closefile)


    def newfile(self):
        print("new file")


    def openfile():
        fname = askopenfilename(filetypes=(("HDF5 files", "*.h5"),
                                           ("All files", "*.*"),
                                           ("jpeg files", "*.jpg") ))
        if fname:
            try:
                print(fname)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        else:
            print("bad file")
        contents = self.readFile(fname)


    def closefile(self):
        print("close file")


    def getObject(self):
        return self.menuFile


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def destroy(self):
        self.menuFile.destroy()



