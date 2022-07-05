#!/usr/bin/python3
""" Read file and print contents to stdout """


def read_file(filename=""):
""" Read file content and print it """
with open(filename) as file:
read_data = file.read()
print(read_data, end="")
