from tkinter import *
from tkinter import ttk
import random
import time
import pika  


class progress():

	def __init__(self):
		self.root = Tk() 
		self.root.title("Messenger")
		self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1)
		self.mainframe['borderwidth'] = 10
		self.mainframe['relief'] = 'sunken'

		ttk.Button(self.mainframe, text="Go!", command=self.loop).grid(column=3, row=3, sticky=W)
		for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
		self.root.mainloop()


	def loop(self):
		for x in range(0, 100):
			time.sleep(.1)			
			connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
			channel = connection.channel()
			channel.queue_declare(queue='test')

			channel.basic_publish(exchange='amq.direct',
			                      routing_key='test',
			                      body="1")
			print(" [x] Sent message")
			connection.close()


app = progress()









