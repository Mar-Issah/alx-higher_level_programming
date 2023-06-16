#!/usr/bin/python3
"""Imported modules for the Base test class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Class to write test cases for the base class"""

    def setUp(self):
        """Method called before each test method"""
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
        self.assertEqual(getattr(Base, "_Base__nb_objects", 0))

if __name__ == '__main__':
    unittest.main()
