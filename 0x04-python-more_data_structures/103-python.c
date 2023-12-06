#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - to print bytes info
 *
 * @p: python object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	long int j, size, lmt;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lmt = 10;
	else
		lmt = size + 1;

	printf("  first %ld bytes:", lmt);

	for (j = 0; j < lmt; j++)
		if (str[j] >= 0)
			printf(" %02x", str[j]);
		else
			printf(" %02x", 256 + str[j]);

	printf("\n");
}

/**
 * print_python_list - to print list info
 *
 * @p: python object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, j;
	PyListObject *lst;
	PyObject *object;

	size = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (j = 0; j < size; j++)
	{
		object = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
