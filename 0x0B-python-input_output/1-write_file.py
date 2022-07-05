#!/usr/bin/python3
""" Open and write into a file """


def write_file(filename="", text=""):
""" Write to a file """
with open(filename, "w") as file:
return file.write(text)
