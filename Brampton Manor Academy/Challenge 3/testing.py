import unittest

from main import *


class MySecondTests(unittest.TestCase):

    def player_One(self):
        self.assertEqual(player_one(), 72)

    def player_Two(self):
        self.assertEqual(player_two(72), 15)

    #def test_custom_num_list(self):
     #   self.assertEqual(len(create_list(10)), 10)

if __name__ == '__main__':
    unittest.main()