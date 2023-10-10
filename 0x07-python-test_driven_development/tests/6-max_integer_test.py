#!/usr/bin/python3

"""The function will add Unittests"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
         """The function for unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test the max in ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test the max value in an unordered list"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with max value at the start"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Case of an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Case of a single element in a given list"""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test a list of floats."""
        floats = [3.64, 7.44, -8.15, 16.4, 7.0]
        self.assertEqual(max_integer(floats), 16.2)

    def test_ints_and_floats(self):
        """Case of diffetnt types"""
        ints_and_floats = [1.35, 17.4, -7, 20, 8]
        self.assertEqual(max_integer(ints_and_floats), 20)

    def test_string(self):
        """If a string"""
        string = "MARIEM"
        self.assertEqual(max_integer(string), 'R')

    def test_list_of_strings(self):
        """list of strings check"""
        strings = ["MARIEM", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Case of None"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
