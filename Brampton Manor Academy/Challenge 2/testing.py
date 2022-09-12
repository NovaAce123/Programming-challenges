import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_joules(self):
        self.assertEqual(joules(3.4), 7943282347.242789)

    def test_tnt(self):
        self.assertEqual(tnt(7943282347.242789), 1.8984900447521006e+18)

    #def test_custom_num_list(self):
     #   self.assertEqual(len(create_list(10)), 10)

if __name__ == '__main__':
    unittest.main()