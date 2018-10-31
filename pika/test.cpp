#include "SimpleAmqpClient/SimpleAmqpClient.h"
#include <iostream>

using namespace std;

int main(){
	AmqpClient::Channel::ptr_t connection = AmqpClient::Channel::Create("localhost");
	
}
