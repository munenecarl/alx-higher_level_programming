#include "main.h"

/**
 * print_python_list_info - prints info about python lists
 * @p: PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i, size, alloc;
	PyObject *item;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}