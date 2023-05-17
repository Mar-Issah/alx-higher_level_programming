#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary.get(value):
        del a_dictionary[value]
    return a_dictionary
