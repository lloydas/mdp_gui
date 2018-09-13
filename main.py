from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import h5py, cv2, os
import pandas as pd
import numpy as np
from PIL import ImageTk, Image



class FileManager():
	def __init__(self):
		self.root = Tk()
		self.root.title("Geostar")
		self.root.option_add('*tearOff', FALSE)
		self.createMenubar()
		self.createMainframe()
		self.createHierarchialFileManager()
		for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
		self.root.mainloop()


	def createMenubar(self):
		self.menubar = Menu(self.root)
		self.root['menu'] = self.menubar

		self.menu_file = Menu(self.menubar)
		self.menu_edit = Menu(self.menubar)
		self.menubar.add_cascade(menu=self.menu_file, label='File')
		self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

		self.menu_file.add_command(label='New', command=self.newFile)
		self.menu_file.add_command(label='Open...', command=self.openFile)
		self.menu_file.add_command(label='Close', command=self.closeFile)


    # menu bar function triggered when "new file" option is clicked
	def newFile(self):
		print("newfile")


    # menu bar function triggered when "open file" option is clicked
	def openFile(self):
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


    # menu bar function triggered when "close file" option is clicked
	def closeFile(self):
		print("closeFile")

	# add hdf5 group and dataset datatypes to class
	def create_hdf5_data_types(self):
		# need a better way to identify type
		throwaway = h5py.File('foo.hdf5','w')
		self.grp = throwaway.create_group("bar")
		self.subgrp = self.grp.create_group("baz")
		self.dset = self.grp.create_dataset("tdset", (1,))
		self.grp_type = self.grp.get(name="baz", getclass=True)
		self.dset_type = self.grp.get(name="tdset", getclass=True)


	def create_new_file_hierarchy(self, filehandle, filename):
		id = self.tree.insert("", 'end', text=self.remove_path_to_file(filename))
		self.create_hdf5_data_types()

		for item in filehandle:
			print(item)
			nextid = self.tree.insert(id, 'end', text=item)
			item_obj = filehandle[item]
			for it in filehandle[item]:
				self.add_to_tree(item_obj, it, nextid)


		# Inserted underneath an existing node:
		# self.tree.insert(id, 'end', text='lol', tags=('onclick'))
		# self.tree.tag_bind('onclick', '<1>', self.itemClicked)


	# triggered when a file is opened
	def readFile(self, filename):
		self.tree = ttk.Treeview(self.mainframe)
		self.tree.grid(column=1, row=0)
		# Inserted at the root, treeview chooses id:
		f = h5py.File(filename, 'r')
		self.create_new_file_hierarchy(f, filename)		

		self.canv = Canvas(self.mainframe, width=40, height=40, bg='white')
		self.canv.grid(column=3, row=0, sticky=(N, W, E, S))
		# self.img = ImageTk.PhotoImage(Image.open(file))  # PIL solution
		# self.canv.create_image(1, 1, anchor=NW, image=self.img)

		f = h5py.File(filename, 'r')
		print("Contents of dataset")
		data = f["ers1"]
		# for datum in data["chan1"]:   uncomment these lines to see raw data (pixels)
		# 	print(datum)


	# rootObj is root node object childString is the name of one of the roots child nodes
	def add_to_tree(self, rootObj, childString, branch_id):
		type = rootObj.get(name=childString, getclass=True)
		if type == self.grp_type:
			atid = self.tree.insert(branch_id, 'end', text=childString + '  |  group')
			for itum in rootObj[childString]:
				self.add_to_tree(rootObj[childString], itum, atid)
		elif type == self.dset_type:
			self.tree.insert(branch_id, 'end', text=childString + '  |  dataset')


	# truncates file path to just name of file
	def remove_path_to_file(self, filepath):
		return filepath.rsplit('/', 1)[-1]


	# creates main window
	def createMainframe(self):
		self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
		self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight= 1)
		

	# function triggered when an item in the file hierarchy is clicked
	def itemClicked(self, arg):
		print("clicked")
		item = self.tree.focus()
		print(item)
		children = self.tree.get_children(item=item)
		child_items = self.tree.item(item = children)
		image = child_items["text"] # this is the file we want to open
		self.open_image(image)


	# creates file hierarchy window
	def createHierarchialFileManager(self):
		self.tree = ttk.Treeview(self.mainframe)
		self.tree.grid(column=1, row=0)
		# Inserted at the root, treeview chooses id:
		id = self.tree.insert("", 'end', text="files")

		# Inserted underneath an existing node:
		self.tree.insert(id, 'end', text='a1.h5', tags=('onclick'))
		self.tree.tag_bind('onclick', '<1>', self.itemClicked)
	
		
x = FileManager()










