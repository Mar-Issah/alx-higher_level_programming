#!/usr/bin/python3
"""Imported module for Rectangle tests class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

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

if __name__ == '__main__':
    unittest.main()
