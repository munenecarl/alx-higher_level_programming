#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <python.h>

void print_python_string(PyObject *p);
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list_info(PyObject *p);


#endif