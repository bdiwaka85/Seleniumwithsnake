'''
Created on Apr 7, 2020

@author: Diwakar
'''
import unittest
from UnitTesting.calculator import Calculator

class test_Calculator(unittest.TestCase):
#the below declaration is what binds the class Calculator to this program so that it can invoke the functions which are inside the class
    test_obj = Calculator()
        
    def test_add(self):
        self.assertEqual(self.test_obj.add(10, 2), 12)
        self.assertEqual(self.test_obj.add(-1, 1), 0)
        self.assertEqual(self.test_obj.add(-5, 4), -1)
        self.assertRaises(TypeError, self.test_obj.add, 'something')
#
    def test_subtract(self):
        self.assertEqual(self.test_obj.subtract(10, 2), 8)
        self.assertEqual(self.test_obj.subtract(-1, 1), -2)
        self.assertEqual(self.test_obj.subtract(-5, -4), -1)
        self.assertRaises(TypeError, self.test_obj.subtract, 'subtract')
#
    def test_multiply(self):
        self.assertEqual(self.test_obj.multiply(3, 2), 6)
        self.assertEqual(self.test_obj.multiply(-1, 1), -1)
        self.assertEqual(self.test_obj.multiply(-5, -4), 20)
#
    def test_divide(self):
        self.assertEqual(self.test_obj.divide(10,2), 5)
        self.assertEqual(self.test_obj.divide(-1, 1), -1)
        self.assertEqual(self.test_obj.divide(-6, -2), 3)
        
        with self.assertRaises(ZeroDivisionError):
            self.test_obj.divide(4,0)

if __name__ == "__main__":
    unittest.main()
