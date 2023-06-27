#!/usr/bin/python3

class Square:
    """Class Square"""
    def __init__(self, size=0):
        """__init__ method.
	Args:
	    size (int): size of the square.
	"""
        self.__size = size
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >=0")

    def area(self):
        """area method.
	Returns:
	    Area of the square.
	"""
        return self.__size ** 2
