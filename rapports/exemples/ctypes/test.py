import ctypes

testlib = ctypes.CDLL('./myexample.so')
testlib.sayHello()
