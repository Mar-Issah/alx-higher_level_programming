#!/usr/bin/python3
"""Imported modules for the Base test class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Class to write test cases for the base class"""

    def setUp(self):
        """Method called before each test method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Method called after each test method"""
        pass

    def test_constructor_with_id(self):
        """Test constructor with id variable"""
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        """Test constructor without id"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_class_variable_exists(self):
        """Test if __nb_objects exists"""
        base_instance = Base()
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_private_class_variable_initial_value(self):
        """Test if __nb_objects has an initial value of 0"""
        base_instance = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)
        self.assertEqual(base_instance._Base__nb_objects, 1)

    def test_to_json_string(self):
        """Test for to_json_string method with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

        """Test with list of dictionaries"""
        data = [
            {"id": 1, "name": "Marsiya"},
            {"id": 2, "name": "Issah"}
        ]
        expected_output = '[{"id": 1, "name": "Marsiya"}, {"id": 2, "name": "Issah"}]'
        self.assertEqual(Base.to_json_string(data), expected_output)

        """ Test with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test for from_json_string method with empty string"""
        self.assertEqual(Base.from_json_string(""), [])

        """Test with JSON string"""
        json_string = '[{"id": 1, "name": "Marsiya"}, {"id": 2, "name": "Issah"}]'
        expected_output = [
            {"id": 1, "name": "Marsiya"},
            {"id": 2, "name": "Issah"}
        ]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        """ Test with None"""
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == '__main__':
    unittest.main()
