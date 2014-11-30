#include <iostream>

extern "C" void sayHello() {
	std::cout << "Hello world" << std::endl;
}
