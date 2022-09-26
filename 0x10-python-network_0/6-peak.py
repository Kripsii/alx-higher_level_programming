#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Return peak in integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
