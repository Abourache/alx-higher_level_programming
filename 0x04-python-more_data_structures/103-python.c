#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_bytes - gives data of the PyBytesObject
 *
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, a = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &s) != -1)
	{
		printf("  size: %zd\n", s);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
		while (a < s + 1 && a < 10)
		{
			printf(" %02hhx", string[a]);
			a++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *item;
	int a = 0;

	if (PyList_CheckExact(p))
	{
		s = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (a < s)
		{
			item = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			a++;
		}
	}
}
