%module myexample
%{
#include "myexample.h"
%}
%include "myexample.h"
%template(IntHello) HelloWorld<int>;
