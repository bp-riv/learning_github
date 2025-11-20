import unittest
from mypackage.main import hello

class Test0(unittest.TestCase):

    def test_0(self):
        self.assertTrue(True)


class Test1(unittest.TestCase):

    def test_1(self):
        self.assertTrue(True)


class Test2(unittest.TestCase):

    def test_2(self):
        hello()
        self.assertTrue(True)


