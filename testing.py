import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(convertmetres(10), 50.292)

    def test_hello(self):
        self.assertEqual(convertfurlong(10), 0.25)

    def test_hello(self):
        self.assertEqual(convertmiles(50.292), 0.03125007767159208)

    def test_hello(self):
        self.assertEqual(convertfeet(50.292), 165.0)

    def test_hello(self):
        self.assertEqual(converttime(0.03125007767159208), 0.6048402129985564)

    #def test_custom_num_list(self):
     #   self.assertEqual(len(create_list(10)), 10)

if __name__ == '__main__':
    unittest.main()