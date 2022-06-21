#!/usr/bin/python3
""" Defines a class square """

class Square:
    """ Defines a square by its size """

    def __init__(self, size=0):
        """ Initialize attribute size with verification """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
