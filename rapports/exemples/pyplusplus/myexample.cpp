#include "boost/python.hpp"
#include "myexample.h"

namespace bp = boost::python;

BOOST_PYTHON_MODULE(pyplusplus){
    { //::hello_world
    
        typedef void ( *hello_world_function_type )(  );
        
        bp::def( 
            "hello_world"
            , hello_world_function_type( &::hello_world ) );
    
    }
}
