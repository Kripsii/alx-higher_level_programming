#!/usr/bin/python3
""" Contains function 'Inherit from-if true/false'. """


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a subclass of a_class. """
    return isinstance(obj, a_class) and type(obj) != a_class
