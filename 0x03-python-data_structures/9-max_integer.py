#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    else:
        # create a copy, sort and return the last element
        copied_list = my_list.copy()
        copied_list.sort()
        return copied_list[-1]
