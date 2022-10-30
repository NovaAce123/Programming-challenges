import unittest

from main import *


class MySecondTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(calc('6','6','6','6','6','6'), True)

    def test2(self):
        self.assertEqual(calc('1','4','2','8','5','7'), False)


if __name__ == '__main__':
    unittest.main()