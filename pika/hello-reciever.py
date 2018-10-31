from tkinter import *
from tkinter import ttk
import random, time, pika, threading


class progress_bar():

	def create_bar(self):
		print("yo")
		progress_bar = Tk()
		progress_bar.title("percent complete")
		self.counter = 0
		self.pgb = ttk.Progressbar(progress_bar, orient="horizontal", value=self.counter, length=500, mode="determinate")
		for child in progress_bar.winfo_children(): child.grid_configure(padx=5, pady=5)
		self.pgb.mainloop()

	def open_connection(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
		channel = connection.channel()
		# channel.exchange_declare(exchange='amq.direct',
                         # exchange_type='direct')
		result = channel.queue_declare(exclusive=True)
		queue_name = result.method.queue
		channel.queue_bind(exchange='amq.direct',
                       queue=queue_name,
                       routing_key="test")

		channel.basic_consume(self.callback,
		                      queue=queue_name,
		                      no_ack=True)

		print(' [*] Waiting for messages. To exit press CTRL+C')
		channel.start_consuming()


	def callback(self, ch, method, properties, body):
		print(" [x] Received %r" % body.decode('UTF-8'))
		self.pgb["value"] += int(body.decode('UTF-8'))
			

	
p = progress_bar()

# create thread for visual progress bar
# p_bar = p.create_bar
# prog_bar_thread = threading.Thread(target=p_bar)
# prog_bar_thread.start()

# create thread for receiving messages
consumer = p.open_connection
consume_messages_thread = threading.Thread(target=consumer)
consume_messages_thread.start()

p.create_bar()











