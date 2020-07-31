#include <Python/Python.h>

int main(int argc, char const *argv[])
{
	Py_Initialize();                       /* init python */
    PyRun_SimpleString("print('Hello embedded world!')");
 
    /* use C extension module above */
    PyRun_SimpleString(
    	 "i = 0\n"
         "for i in range(10000):\n"
         	 "\tprint(i)\n");
 
    PyRun_SimpleString("print('Bye embedded world!')");
	return 0;
}