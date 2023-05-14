#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Prints info about a Python list obj
 * @p: reference to the Python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int idx;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));

	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (idx = 0; idx < Py_SIZE(p); idx++)
		printf("Element %d: %s\n", idx, Py_TYPE(PyList_GetItem(p, idx))->tp_name);
}
