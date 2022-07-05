#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Representation of square by size """

    def __init__(self, size=0):
        """ Initialize size attribute with validation """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """ Return current area of square """
            return self.__size ** 2
