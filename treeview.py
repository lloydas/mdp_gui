from tkinter import *
from tkinter import ttk
import h5py


class treeview:
    def __init__(self, parent=None, values={}, position={}):
        self.treeObject = ttk.Treeview(parent)
        self.state = dict()     
        self.state["visible"] = False
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.rootFileNodeId = self.treeObject.insert("", 'end', text="Files")
        self.createWidgets()
        self.render()


    def createWidgets(self):
        if self.values is not None:
            for val in self.values:
                self.treeObject[val] = self.values[val]


    def getObject(self):
        return self.treeObject


    def setState(self, state):
        self.state = state


    def getState(self):
        return self.state


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            self.treeObject.grid(column=self.position["column"])
        if "row" in self.position:
            self.treeObject.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.treeObject.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.treeObject.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.treeObject.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.treeObject.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.treeObject.grid(rowspan=self.position["rowspan"])
        self.treeObject.grid()


    def destroy(self):
        self.treeObject.destroy()


    # add hdf5 group and dataset datatypes to class
    def create_hdf5_data_types(self):
        # need a better way to identify type
        throwaway = h5py.File('foo.hdf5','w')
        grp = throwaway.create_group("bar")
        subgrp = grp.create_group("baz")
        dset = grp.create_dataset("tdset", (1,))
        self.grp_type = grp.get(name="baz", getclass=True)
        self.dset_type = grp.get(name="tdset", getclass=True)


    # rootObj is root node object childString is the name of one of the roots child nodes
    def add_to_tree(self, rootObj, childString, branch_id):
        type = rootObj.get(name=childString, getclass=True)
        if type == self.grp_type:
            atid = self.treeObject.insert(branch_id, 'end', text=childString + '  |  group')
            for itum in rootObj[childString]:
                self.add_to_tree(rootObj[childString], itum, atid)
        elif type == self.dset_type:
            self.treeObject.insert(branch_id, 'end', text=childString + '  |  dataset')


    # truncates file path to just name of file
    def remove_path_to_file(self, filepath):
        return filepath.rsplit('/', 1)[-1]

    # adds file to file tree
    def addFile(self, filename):
        f = h5py.File(filename, 'r')
        self.fileId = self.treeObject.insert("", 'end', text=self.remove_path_to_file(filename))
        self.create_hdf5_data_types()

        for item in f:
            nextid = self.treeObject.insert(self.fileId, 'end', text=item)
            item_obj = f[item]
            for it in f[item]:
                self.add_to_tree(item_obj, it, nextid)

    def removeFile(self):
        self.treeObject.delete(self.fileId)

