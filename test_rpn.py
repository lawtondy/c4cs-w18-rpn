import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_multiply(self):
        result = rpn.calculate('3 4 *')
        self.assertEqual(12, result)
    def test_divide(self):
        result = rpn.calculate('6 2 /')
        self.assertEqual(3, result)
    def test_factorial(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)
    def test_summation(self):
        result = rpn.calculate('1 2 3 4 5 ?')
        self.assertEqual(15, result)
    def test_and(self):
        result = rpn.calculate('5 3 &')
        self.assertEqual(1, result)
    def test_or(self):
        result = rpn.calculate('5 2 |')
        self.assertEqual(7, result)
    def test_not(self):
        result = rpn.calculate('60 ~')
        self.assertEqual(-61, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
    def test_exp(self):
        result = rpn.calculate('3 2 ^')
        self.assertEqual(9, result)
