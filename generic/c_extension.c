#include <Python.h>
#include "src/custom.h"
 
// base reference function to a function that takes int arg
// this function encapsulates 'test_func'  
static PyObject* callInt(PyObject* self, PyObject* args)
{
    int n;
 
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    
    return Py_BuildValue("i", test_func(n));
}


static PyMethodDef moduleMethods[] = {
    {"call_int", callInt, METH_VARARGS, "call this function with int argument"},
    // TODO - add function calls here {name_in_python - str, name_in_c - reff, argstype, description}
    // e.g. - {"call_string", callInt, METH_VARARGS, "call this function with int argument"},
    {NULL, NULL, 0, NULL}
};
 
static struct PyModuleDef cModule = {
	PyModuleDef_HEAD_INIT,
	"cModule",
	"generic cModule",
	-1,
	moduleMethods
};

PyMODINIT_FUNC PyInit_cModule(void)
{
    return PyModule_Create(&cModule);
}