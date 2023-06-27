#!/usr/bin/python3

class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Class Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """area method.
	Returns:
	    Area of the square.
	"""
        return self.__size ** 2

    @property
    def size(self):
        """size method.
	Returns: size of the square.
	"""
        return self.__size

    @size.setter
    def size(self, value):
        """size method.
        Args:
            value (int): size of the square.
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
