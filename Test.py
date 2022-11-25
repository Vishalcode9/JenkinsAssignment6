import unittest
from perfectsquare import isPerfectSquare
class TestisPerfectSquare(unittest.TestCase):
    def test_case1(self):
        result = isPerfectSquare(5)
        self.assertEqual(result,False)
    def test_case2(self):
        result = isPerfectSquare(6)
        self.assertEqual(result,False)
    def test_case3(self):
        result = isPerfectSquare(7)
        self.assertEqual(result,False)
    def test_case4(self):
        result = isPerfectSquare(4)
        self.assertEqual(result,True)
    def test_case5(self):
        result = isPerfectSquare(3)
        self.assertEqual(result,False)

if __name__ == '__main__':
    unittest.main()
