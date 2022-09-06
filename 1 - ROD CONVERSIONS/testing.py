import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(convertmetres(10), 'hello world')

    def test_hello(self):
        self.assertEqual(convertfurlong(), 'hello world')

    def test_hello(self):
        self.assertEqual(convertmetres(), 'hello world')

    def test_hello(self):
        self.assertEqual(convertmetres(), 'hello world')

    def test_hello(self):
        self.assertEqual(convertmetres(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_list(10)), 10)
