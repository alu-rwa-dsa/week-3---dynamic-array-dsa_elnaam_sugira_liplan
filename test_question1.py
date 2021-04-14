import unittest
from unittest.case import TestCase
from question3_1 import ArrayClass


class test_q3(unittest.TestCase):
    def test_c1(self):
        x = ArrayClass()
        x.__set__(23, 0)
        self.assertEqual(x.__len__(), 1)

    def test_c3(self):
        x2 = ArrayClass()
        self.assertEqual(x2.__len__(), 0)

    
if __name__ == "__main__":
    unittest.main()
