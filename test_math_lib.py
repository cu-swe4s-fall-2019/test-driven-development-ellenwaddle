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

    def test_list_mean_rand_ints(self):
        L=[]
        for i in range(100):
            for j in range(10):
                L.append(
                    random.randint(0,100))
                r=math_lib.list_mean(L)
                e=statistics.mean(L)
                self.assertEqual(r,e)

    def test_list_mean_rand_floats(self):
        L=[]
        for i  in range(100):
            for j in range(10):
                L.append(
                    random.uniform(0,100))
            r=math_lib.list_mean(L)
            e=statistics.mean(L)
            self.assertAlmostEqual(r,e)

    def test_list_mean_non_int(self):
        L=[]
        for i in range(10):
            L.append(random.randint(0,100))
        e=statistics.mean(L)
        L.append('X')
        r=math_lib.list_mean(L)
        self.assertEqual(e,r)

    def test_list_stdev_empty_list(self):
        r=math_lib.list_stdev(None)
        self.assertEqual(r,None)

    def test_list_stdev_constant(self):
        r=math_lib.list_stdev([2,2,2,2])
        self.assertEqual(r,0)


if __name__=='__main__':
    unittest.main()
