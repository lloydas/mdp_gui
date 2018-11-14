#include <SimpleAmqpClient/SimpleAmqpClient.h>
#include <iostream>
#include <unistd.h>

using namespace std; 
// to compile main program
// g++ --std=c++11 -Wall -pedantic -Werror test.cpp /Users/andrewlloyd/Documents/fall_2018/gui-mdp/mdp_gui/pika/SimpleAmqpClient/simpleamqpclient-build/libSimpleAmqpClient.dylib  -o test
// to create libfoo.so file
// g++ -c -fPIC --std=c++11 -Wall -pedantic -Werror test.cpp -o test.o
// g++ -shared -Wl,-install_name,libfoo.so -I/Users/andrewlloyd/Documents/fall_2018/gui-mdp/mdp_gui/pika/SimpleAmqpClient/src/SimpleAmqpClient -o libfoo.so test.o
// g++ -shared -Wl,-install_name,libfoo.so -I/Users/andrewlloyd/Documents/fall_2018/gui-mdp/mdp_gui/pika/SimpleAmqpClient/src/SimpleAmqpClient -o libfoo.so test.o
 
// working compile statement
// g++ --std=c++11 -Wall -pedantic -Werror -shared -Wl,-install_name,libfoo.so test.cpp /Users/andrewlloyd/Documents/fall_2018/gui-mdp/mdp_gui/pika/SimpleAmqpClient/simpleamqpclient-build/libSimpleAmqpClient.dylib -o libfoo.so test

// int main(){
// 	// AmqpClient::Channel::ptr_t connection = AmqpClient::Channel::Create("localhost");
// 	 // Smallest frame size allowed by AMQP
//   	AmqpClient::Channel::ptr_t channel = AmqpClient::Channel::Create("localhost",
//                                            5672, "guest", "guest", "/", 4096);
//   	for(int i = 0; i < 100; ++i){
//   		usleep(150000);
//   		AmqpClient::BasicMessage::ptr_t message = AmqpClient::BasicMessage::Create("1");
//   		channel->BasicPublish("amq.direct", "test", message); 
//   	}
  	
// }
class Messenger{
public:
	void send(){
		AmqpClient::Channel::ptr_t channel = AmqpClient::Channel::Create("localhost",
                                           5672, "guest", "guest", "/", 4096);
		for(int i = 0; i < 100; ++i){
  			usleep(150000);
  			AmqpClient::BasicMessage::ptr_t message = AmqpClient::BasicMessage::Create("1");
  			channel->BasicPublish("amq.direct", "test", message); 
  		}
	}
};

extern "C" {
	Messenger* createMessenger(){ return new Messenger(); }
	void sendMessage(Messenger *m){ m->send(); }
}




