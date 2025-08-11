test_simple_calculator.py
# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """A test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up a new instance of SimpleCalculator for each test method."""
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the add method with positive numbers."""
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(10, -5), 5)

    def test_subtract(self):
        """Test the subtract method with various numbers."""
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(5, 10), -5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiply method with different numbers, including zero."""
        self.assertEqual(self.calculator.multiply(5, 5), 25)
        self.assertEqual(self.calculator.multiply(10, 0), 0)
        self.assertEqual(self.calculator.multiply(-2, 8), -16)

    def test_divide(self):
        """Test the divide method with normal and edge cases."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(100, 10), 10)
        self.assertEqual(self.calculator.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test the divide method when the denominator is zero."""
        self.assertIsNone(self.calculator.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
