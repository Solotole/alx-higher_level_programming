#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class passing Testcase"""
    def test_max_integer(self):
        """method resposible for tesing perfomance of code"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 6, 89, 12, 92]), 92)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([0, -12]), 0)
        self.assertEqual(max_integer([0, 78]), 78)
        self.assertEqual(max_integer([-12, 0, 12]), 12)
        self.assertEqual(max_integer([1, -1 , -938, -934]), 1)
    if __name__ == '__main__':
        unittest.main()
