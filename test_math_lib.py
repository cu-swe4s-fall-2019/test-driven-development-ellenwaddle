import unittest
import math_lib
import statistics
import random

class TestMathLib(unittest.TestCase):
    def test_list_mean_empty_list(self):
        r=math_lib.list_mean(None)
        self.assertEqual(r,None)

    def test_list_mean_constant(self):
        r=math_lib.list_mean([2,2,2,2])
        self.assertEqual(r,2)

if __name__=='__main__':
    unittest.main()
