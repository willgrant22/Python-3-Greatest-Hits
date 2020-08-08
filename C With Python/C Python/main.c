#include <Python/Python.h>

int main(int argc, char const *argv[])
{
	Py_Initialize();                       /* init python */
    PyRun_SimpleString("print('Hello embedded world!')");
 
    /* use C extension module above */
    PyRun_SimpleString(
    	 "i = 0\n"
         "for i in range(100):\n"
         	 "\ti = i + 1\n"
         	 "\tfile = open('txt/file_%s.txt' % i, 'wb')\n"
         	 "\tfile.write('whatever')\n"
             "\tfile.close()\n");
 
    PyRun_SimpleString("print('Bye embedded world!')");
	return 0;
}