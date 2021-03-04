import unittest
import pytest
import sys
from fibonacci import factorial, fibonacci

class TestFibbonaci(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fib2(self):
        self.assertEqual(fibonacci(2), 1)
    def test_fib3(self):
        self.assertEqual(fibonacci(3), 2)
    def test_fib4(self):
        self.assertEqual(fibonacci(4), 3)
    def test_fib5(self):
        self.assertEqual(fibonacci(5), 5)
    def test_fibNeg(self):
        self.assertEqual(fibonacci(-6), None)
    def test_fibString(self):
        self.assertEqual(fibonacci("7"), None)
    def test_fac1(self):
        self.assertEqual(factorial(1), 1)
    def test_fac2(self):
        self.assertEqual(factorial(2), 2)
    def test_fac3(self):
        self.assertEqual(factorial(3), 6)
    def test_fac4(self):
        self.assertEqual(factorial(4), 24)
    def test_fac5(self):
        self.assertEqual(factorial(5), 120)
    def test_facNeg(self):
        self.assertEqual(factorial(-6), None)
    def test_facString(self):
        self.assertEqual(factorial("7"), None)


if __name__ == '__main__':
    unittest.main()