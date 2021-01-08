#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_interger(self):
        """Test output of max_interger()
        """
        self.assertAlmostEqual(max_integer([1, 2, 5, 4, 8]), 8)
        self.assertAlmostEqual(max_integer([-8, 2, -1, 5]), 5)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([1, 1, 1]), 1)
        self.assertAlmostEqual(max_integer([-1, 0, 1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
