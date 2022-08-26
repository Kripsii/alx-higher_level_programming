#!/usr/bin/python3
""" Append to a file. """


def append_write(filename="", text=""):
	""" Append text to a file """
	with open(filename, "a") as file:
	return file.write(text)
