#!/usr/bin/python3
""" Read file and output stdout. """


def read_file(filename=""):
    """ Prints read file contents. """
    with open(filename) as file:
        read_data = file.read()
        print(read_data, end="")
