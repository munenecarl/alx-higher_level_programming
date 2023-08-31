#!/usr/bin/python3

"""this module contains a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """This function divides all elements of a matrix.

    Args:
	matrix (list): matrix to be divided.
	div (int): number to divide the matrix by.

    Returns:
	list: new matrix with divided elements.

    Raises:
	TypeError: If matrix is not a list of lists of integers or floats.
	TypeError: If matrix is not a rectangle (all rows are not the same size).
	TypeError: If div is not an integer or float.
	ZeroDivisionError: If div is equal to 0.
    """

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(matrix[0]) == 0:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            elif type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                return [[round(element / div, 2) for element in row] for row in matrix]
