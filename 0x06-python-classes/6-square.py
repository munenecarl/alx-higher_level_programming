#!/usr/bin/python3

class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Class Square"""
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """position method.
    Returns: position of the square.
    """
        return self.__position
    
    @position.setter
    def position(self, value):
        """position method.
        Args:
            value (int): position of the square.
        """
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    def my_print(self):
        """my_print method.
	Args:
	    size (int): size of the square.
	"""
        if self.__size == 0:
	        print()
        else:
	        for i in range(self.__size):
		        print("#" * self.__size)
