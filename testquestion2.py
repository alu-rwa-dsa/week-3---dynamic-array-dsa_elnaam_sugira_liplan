import unittest
from question2 import DynamicArray


class testq2(unittest.TestCase):
    def test_c1(self):
        ardy1 = DynamicArray()
        ardy1.add(57)
        self.assertEqual(ardy1.__get__(0), 57)

    def test_c2(self):
        ardy1 = DynamicArray()
        ardy1.add(57)
        self.assertEqual(ardy1.__len__(), 1)

    def test_c3(self):
        ardy1 = DynamicArray()
        ardy1.add(57)
        ardy1.add(7)
        self.assertEqual(ardy1.__len__(), 2)

    def test_c4(self):
        ardy1 = DynamicArray()
        ardy1.add(57)
        ardy1.dele()
        self.assertEqual(ardy1.__len__(), 0)


if __name__ == "__main__":
    unittest.main()
