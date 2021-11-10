#include <stdio.h>
#include <Python/Python.h>
#include <iostream>

int
main(int argc, char** argv)
{
    Py_Initialize();

    // First set in path where to find your custom python module.
    // You have to tell the path otherwise the next line will try to load
    // your module from the path where Python's system modules/packages are
    // found.
    PyObject* sysPath = PySys_GetObject("path");
    PyList_Append(sysPath, PyString_FromString("/Users/will/Library/Mobile Documents/com~apple~CloudDocs/MEGAsync/Software Development/GitHub/Python-3-Greatest-Hits/C With Python/C++ Python"));

    // Load the module
    PyObject *pName = PyString_FromString("my_mod");
    PyObject *pModule = PyImport_Import(pName);

    // Random use-less check
    std::cout<< "Works fine till here\n";

    if (pModule != NULL) {
        std::cout << "Python module found\n";

        // Load all module level attributes as a dictionary
        PyObject *pDict = PyModule_GetDict(pModule);

        // Remember that you are loading the module as a dictionary, the lookup you were
        // doing on pDict would fail as you were trying to find something as an attribute
        // which existed as a key in the dictionary
        PyObject *pFunc = PyDict_GetItem(pDict, PyString_FromString("my_func"));
        

        if(pFunc != NULL){
            PyObject_CallObject(pFunc, NULL);
        } else {
            std::cout << "Couldn't find func\n";
        }
    }
    else
        std::cout << "Python Module not found\n";
    return 0;
}