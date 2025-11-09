#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_one_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        """Test with all elements being equal"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.9]), 3.3)

    def test_mixed_int_float(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 2.9]), 3)

    def test_string_list(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_single_string(self):
        """Test with a single string (should return max char)"""
        self.assertEqual(max_integer("abcxyz"), "z")


if __name__ == '__main__':
    unittest.main()
