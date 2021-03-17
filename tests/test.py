#!/usr/bin/env python
import unittest
from code.test_functions import test_sum


class TestHello(unittest.TestCase):
    def test_simple_sum(self):
        simple_result = test_sum(1, 1)
        self.assertEqual(simple_result, 2)


if __name__ == "__main__":
    unittest.main()
