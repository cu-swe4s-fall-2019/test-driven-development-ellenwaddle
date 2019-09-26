import unittest
import sys
import data_viz as dv

class TestDataViz(unittest.TestCase):

    def test_data_viz_boxplot_name_already_exists(self):
        r=dv.boxplot([1,2,3,4],'empty.txt')
        self.assertEqual(r,'this file name is taken, choose another.')

    def test_data_viz_histogram_plotname_exists_after_running(self):
        r=dv.histogram([1,2,3,5,6,2,1]

if __name__=='__main__':
    unittest.main()
