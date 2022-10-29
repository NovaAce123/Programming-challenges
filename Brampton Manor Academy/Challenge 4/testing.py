import unittest

from main import *


class MySecondTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(TempCalc(10,15), -6.5895344209562525)

    def test2(self):
        self.assertEqual(TempCalc(0,25), -24.093780999553864)

    def test3(self):
        self.assertEqual(TempCalc(-10,35), -41.16894662953316)
    
    def test4(self):
        self.assertEqual(TempCalc(3.5,18), -16.47884113003356)

if __name__ == '__main__':
    unittest.main()