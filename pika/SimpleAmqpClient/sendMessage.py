from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')
 
# to compile 
# g++ -c -fPIC --std=c++11 -Wall -pedantic test.cpp -I/Users/andrewlloyd/Documents/fall_2018/gui-mdp/mdp_gui/pika/SimpleAmqpClient/simpleamqpclient-build/libSimpleAmqpClient.dylib  -o test.o
# g++ -shared -Wl,-install_name,libfoo.so -o libfoo.so -fPIC test.o

class Messenger(object):
    def __init__(self):
        self.obj = lib.createMessenger()

    def send(self):
        lib.sendMessage(self.obj)


obj = Messenger()
obj.send()

