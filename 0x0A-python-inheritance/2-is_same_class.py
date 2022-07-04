#!/usr/bin/python3
""" Defining the function is_same_class. """


def is_same_class(obj, a_class):
    """ True if the object is exactly an instance of the a_class. """
    return type(obj) == a_class
