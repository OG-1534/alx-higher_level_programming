#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print out basic information
 * on Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocate, x;
	const char *type;
	PyListObject *lst = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	size = variable->ob_size;
	allocate = lst->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocate);

	for (x = 0; x < size; x++)
	{
		type = lst->ob_item[x]->ob_type->tp_name;
		printf("Element %ld: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(lst->ob_item[x]);
		else if (strcmp(type, "float") == 0)
			print_python_float(lst->ob_item[x]);
	}
}

/**
 * print_python_bytes - print out basic information
 * on Python byte objects.
 * @p: object of PyObject byte.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, x;
	PyBytesObject *byte = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byte->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (x = 0; x < size; x++)
	{
		printf("%02hhx", byte->ob_sval[x]);
		if (x == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints out basic information
 * on Python float objects.
 * @p: object of PyObject float.
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}
