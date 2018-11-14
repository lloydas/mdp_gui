from tkinter import *
from tkinter import ttk
from frame import frame
from button import button
from canvas import canvas
from treeview import treeview
from menuBar import menuBar
from menuFile import menuFile
from label import label
from entry import entry
from text import text
from progressBar import progressBar
import json, pika, time, threading


def loopWrapper():
	t = threading.Thread(target=loop)
	t.start()


def loop():
	for x in range(0, 100):
		time.sleep(.1)			
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		channel = connection.channel()
		channel.queue_declare(queue='prog_queue')

		channel.basic_publish(exchange='',
		                      routing_key='prog_queue',
		                      body="1")
		print(" [x] Sent message")
		connection.close()


with open("values.json") as values_file:
	values_json = json.load(values_file)

root = Tk()


def createCanvas():
	newWindow = Toplevel()
	newWindow.geometry("500x500")

	newCanvas = canvas(newWindow, values_json["canvas"][0], values_json["canvas"][1])
	entry1 = entry(newWindow, values_json["entry1"][0], newCanvas)
	entry1.render(values_json["entry1"][1])
	buttonCanvas = button(newWindow, entry1.getTextVal, values_json["buttonCanvas"][0], values_json["buttonCanvas"][1])



content = frame(root, values_json["content"][0], values_json["content"][1])
tree = treeview(content.getObject())
tree.addFile("a1.h5")
tree.addFile("a1.h5")
frame = frame(content.getObject(), values_json["frame"][0], values_json["frame"][1])
frame1 = frame.getObject()
button1 = button(frame1, frame1.quit, values_json["button"][0], values_json["button"][1])
label = label(content.getObject(), values_json["label"][0], values_json["label"][1])
# entry = entry(content.getObject(), values_json["entry"][0], values_json["entry"][1])
# entry.render()
textBig = text(content.getObject(), values_json["textBig"][0], values_json["textBig"][1])
buttonPrintEntry = button(frame1, entry.getTextVal, values_json["buttonEntry"][0], values_json["buttonEntry"][1])
buttonPrintText = button(frame1, textBig.getTextVal, values_json["buttonText"][0], values_json["buttonText"][1])
progBar = progressBar(content.getObject(), values_json["progressBar"][0], values_json["progressBar"][1])
buttonProgBar = button(frame1, progBar.step, values_json["progButton"][0], values_json["progButton"][1])
menubar = menuBar(frame1, position=values_json["menubar"][0])
menuFile = menuFile(menubar.getObject())
menubar.addMenuFile("File", menuFile.getObject())

trigger = button(frame1, createCanvas, values_json["buttonTrigger"][0], values_json["buttonTrigger"][1])

root.mainloop()

