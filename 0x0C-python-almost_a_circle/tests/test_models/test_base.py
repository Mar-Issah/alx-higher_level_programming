#!/usr/bin/python3
"""Imported modules for the Base test class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
from models.square import Square

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

    def test_save_to_file(self):
        """ Create a list of Rectangle objects"""
        rectangles = [
            Rectangle(4, 6, 2, 3),
            Rectangle(5, 3, 1, 2)
        ]

        Rectangle.save_to_file(rectangles)

        filename = Rectangle.__name__ + ".json"
        with open(filename, "r") as file:
            content = file.read()

        self.assertTrue(content.startswith("["))
        self.assertTrue(content.endswith("]"))

        json_data = Rectangle.from_json_string(content)

        self.assertEqual(len(rectangles), len(json_data))

        for orig_rect, saved_rect_dict in zip(rectangles, json_data):
            self.assertEqual(orig_rect.to_dictionary(), saved_rect_dict)

        os.remove(filename)

        rectangles = [
                Rectangle(4, 6, 2, 3),
                Rectangle(5, 3, 1, 2)
            ]

        """Save and read the rectangles to a file"""
        Rectangle.save_to_file(rectangles)

        filename = Rectangle.__name__ + ".json"
        with open(filename, "r") as file:
            content = file.read()


        self.assertTrue(content.startswith("["))
        self.assertTrue(content.endswith("]"))


        json_data = Rectangle.from_json_string(content)

        self.assertEqual(len(rectangles), len(json_data))

        for orig_rect, saved_rect_dict in zip(rectangles, json_data):
            self.assertEqual(orig_rect.width, saved_rect_dict["width"])
            self.assertEqual(orig_rect.height, saved_rect_dict["height"])
            self.assertEqual(orig_rect.x, saved_rect_dict["x"])
            self.assertEqual(orig_rect.y, saved_rect_dict["y"])
            self.assertEqual(orig_rect.id, saved_rect_dict["id"])

        os.remove(filename)

    def test_create_rectangle(self):
        """ Create a dictionary with values for a Rectangle"""
        rect_dict = {"id": 1, "width": 5, "height": 3, "x": 2, "y": 1}


        rect = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect, Rectangle)

        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_create_square(self):
        """ Create a dictionary with values for a Square"""
        square_dict = {"id": 20, "size": 4, "x": 9, "y": 22}

        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)

        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 22)


if __name__ == '__main__':
    unittest.main()
