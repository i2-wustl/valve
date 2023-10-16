import unittest

class SimpleTest(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(1 + 1, 2)
