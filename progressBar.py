from tkinter import *
from tkinter import ttk
import pika, threading

class progressBar():
    def __init__(self, parent=None, values={}, position={}):
        self.object = ttk.Progressbar(parent)
        self.state = dict()
        self.state["visible"] = True
        self.state["rendered"] = False
        self.values = values
        self.position = position
        self.createWidgets()
        self.render()
        self.t = threading.Thread(target=self.open_connection)
        self.t.start()


    def step(self):
    	print("triggered")
    	self.object.step(5)

    def createWidgets(self):
        for val in self.values:
            self.object[val] = self.values[val]


    def getObject(self):
        return self.object


    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def render(self):
        self.state["rendered"] = True
        self.state["visible"] = True
        if "column" in self.position:
            self.object.grid(column=self.position["column"])
        if "row" in self.position:
            self.object.grid(row=self.position["row"])
        if "sticky" in self.position:
            self.object.grid(sticky=self.position["sticky"])
        if "padx" in self.position:
            self.object.grid(padx=self.position["padx"])
        if "pady" in self.position:
            self.object.grid(pady=self.position["pady"])
        if "columnspan" in self.position:
            self.object.grid(columnspan=self.position["columnspan"])
        if "rowspan" in self.position:
            self.object.grid(rowspan=self.position["rowspan"])
        self.object.grid()


    def destroy(self):
        self.object.destroy()


    def open_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = self.connection.channel()
        channel.queue_declare(queue='prog_queue')

        channel.basic_consume(self.callback,
                              queue='prog_queue',
                              no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body.decode('UTF-8'))
        self.object["value"] += int(body.decode('UTF-8'))
        if self.object["value"] == 100:
        	self.destroy()
        	self.connection.close()




