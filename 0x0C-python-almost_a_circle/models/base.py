#!/usr/bin/python3
"""Imported modules for the Base class"""
from json import dumps
from json import loads


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)
