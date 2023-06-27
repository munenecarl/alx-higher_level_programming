#!/usr/bin/python3

class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Class Square"""
        self.__size = size
        if type(size) is not int:
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >=0")
