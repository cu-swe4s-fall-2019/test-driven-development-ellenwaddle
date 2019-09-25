import unittest
import get_data

class TestGetData(unittest.TestCase):
    def test_get_data_no_columns(self):
        r=get_data.read_stdin_col(None)
        self.assertEqual(r,None)
