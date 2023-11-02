# from calculator import calculator
import unittest

# newcalculator = calculator()

def add(num1,num2):
    return num1 + num2

class testAdd(unittest.TestCase):
    def test_positive_negative(self):
        result = add('55',-55)
        self.assertEqual(result,0)



unittest.main()

