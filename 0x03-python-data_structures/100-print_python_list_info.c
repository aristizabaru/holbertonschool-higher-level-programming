#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - Print information about a pyhton list object
 * @p: python object
 * Description: Prints lenght, allocated memory and data types of the object (list)
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
        int i = 0;
        if (p)
        {
                printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
                printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
                for (i = 0; i < PyList_Size(p); i++)
                {
                        if (PyTuple_Check(PyList_GetItem(p, i)))
                                printf("Element %d: tuple\n", i);
                        else if (PyFloat_Check(PyList_GetItem(p, i)))
                                printf("Element %d: float\n", i);
                        else if (PyLong_Check(PyList_GetItem(p, i)))
                                printf("Element %d: int\n", i);
                        else if (PyUnicode_Check(PyList_GetItem(p, i)))
                                printf("Element %d: str\n", i);
                        else if (PyList_Check(PyList_GetItem(p, i)))
                                printf("Element %d: list\n", i);
                }
        }
}
