#include <boost/python.hpp>
#include "myexample.h"

BOOST_PYTHON_MODULE(myexample)
{
	using namespace boost::python;
	class_< HelloWorld< int > >( "IntHello" )
		.def( 
			"multiply"
			, (int ( ::HelloWorld<int>::* )( int,int ) )( &::HelloWorld< int >::multiply )
			, ( arg("x"), arg("y") ) )
		.def( 
			"sayHello"
			, (void ( ::HelloWorld<int>::* )(  ) )( &::HelloWorld< int >::sayHello ) );
}

