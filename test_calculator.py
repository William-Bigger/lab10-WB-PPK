# https://github.com/William-Bigger/lab10-WB-PPK
# Partner 1: William Bigger
# Partner 2: Poojha Praveen Kumar


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 4), 0)
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(-4, 2), -6)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(-2, 1), -2)
        self.assertEqual(multiply(2, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(4, 20), 5)
        self.assertEqual(divide(-2, 10), -5)
        self.assertAlmostEqual(divide(8, 4), 0.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(2, 0), 2)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356237)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(1), 1)
        with self.assertRaises(ValueError):
            square_root(-25)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()