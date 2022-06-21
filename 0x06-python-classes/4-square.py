#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Definition of a square by its size """

    def __init__(self, size=0):
        """ Initialize size attribute """
        self.__size = size

        @property
        def size(self):
            """ Get size """
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """ Return are of current square """
                return self.__size ** 2
