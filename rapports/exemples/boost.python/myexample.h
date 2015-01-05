#include <iostream>

template <class T> 
class HelloWorld
{
public:
	inline
	void sayHello() {
		std::cout << "Hello world" << std::endl;
	}
	inline
	T multiply(T x,T y)
	{
		return x*y;
	}
};
