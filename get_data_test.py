import unittest
import get_data
import sys


class TestGetData(unittest.TestCase):

    def test_get_data_no_columns(self):
        r = get_data.read_stdin_col(0)
        self.assertEqual(r, None)

    def test_get_data_one_column(self):
        f = open(getdatatestfile.txt, 'r')
        r = get_data.read_stdin_col(2)
        self.assertEqual(f, r)


if __name__ == '__main__':
    unittest.main()
