from addition import sum
import unittest

class TestAddition(unittest.TestCase):
    def testAddition_1_2(self):
        result = sum(1,2)
        self.assertEqual(result,3)
    def testAddition_negative(self):
        result = sum(-1,-2)
        self.assertEqual(result,-3)

if __name__ == "__main__" :
    unittest.main()
