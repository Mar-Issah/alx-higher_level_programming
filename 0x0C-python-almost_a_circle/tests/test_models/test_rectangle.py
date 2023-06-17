#!/usr/bin/python3
"""Imported module for Rectangle tests class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """This method is called before each test method"""
        pass

    def tearDown(self):
        """This method is called after each test method"""
        pass

    def test_constructor_with_id(self):
        """Test constructor with id"""
        obj = Rectangle(5, 3, 2, 1, 10)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 1)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        """Test constructor without id"""
        obj = Rectangle(5, 3, 2, 1)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 1)
        self.assertIsNone(obj.id)

    def test_getters_and_setters(self):
        """Test getters and setters"""
        obj = Rectangle(5, 3, 2, 1)
        obj.width = 10
        obj.height = 7
        obj.x = 3
        obj.y = 2

        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 2)

    def test_inheritance(self):
        """Test if object is an instance of both classes"""
        obj = Rectangle(5, 3, 2, 1)
        self.assertIsInstance(obj, Rectangle)
        self.assertIsInstance(obj, Base)

    def test_invalid_width(self):
        """Test invalid width"""
        with self.assertRaises(ValueError):
            obj = Rectangle(-5, 3, 2, 1)

    def test_invalid_height(self):
        """Test invalid height"""
        with self.assertRaises(ValueError):
            obj = Rectangle(5, -3, 2, 1)

    def test_invalid_x(self):
        """Test invalid x"""
        with self.assertRaises(ValueError):
            obj = Rectangle(5, 3, "invalid", 1)

    def test_invalid_y(self):
        """Test invalid y"""
        with self.assertRaises(ValueError):
            obj = Rectangle(5, 3, 2, "invalid")

    def test_validate_attribute_inclusive(self):
        """Test validate_attribute method with inclusive flag set to True"""
        rect = Rectangle(5, 3, 2, 1)
        self.assertRaises(TypeError, rect.validate_attribute, "width", "invalid")
        self.assertRaises(ValueError, rect.validate_attribute, "width", -5)
        self.assertRaises(ValueError, rect.validate_attribute, "height", -3)
        self.assertRaises(ValueError, rect.validate_attribute, "x", "invalid")
        self.assertRaises(ValueError, rect.validate_attribute, "y", "invalid")

    def test_validate_attribute_exclusive(self):
        """Test validate_attribute method with inclusive flag set to False"""
        rect = Rectangle(5, 3, 2, 1)
        self.assertRaises(TypeError, rect.validate_attribute, "width", "invalid", False)
        self.assertRaises(ValueError, rect.validate_attribute, "width", 0, False)
        self.assertRaises(ValueError, rect.validate_attribute, "height", 0, False)
        self.assertRaises(ValueError, rect.validate_attribute, "x", "invalid", False)
        self.assertRaises(ValueError, rect.validate_attribute, "y", "invalid", False)

    def test_area(self):
        """Test the area method"""
        rect = Rectangle(5, 3, 2, 1)
        self.assertEqual(rect.area(), 15)

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(5, 3, 2, 1)
        expected_output = "\n\n  #####\n  #####\n  #####\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
