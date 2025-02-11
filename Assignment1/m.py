import pandas as pd

def read_in_range(start_month, start_year, end_month, end_year):
    cur_month, cur_year = start_month, start_year
    dfs = []
    
    while cur_year < end_year or (cur_year == end_year and cur_month <= end_month):
        dfs.append(pd.read_csv("orders_" + str(cur_month) + "-" + str(cur_year) + ".csv"))
        
        cur_month = cur_month + 1 if cur_month < 12 else 1
        cur_year = cur_year + 1 if cur_month == 1 else cur_year
    
    return pd.concat(dfs, ignore_index=True)


import unittest
from unittest.mock import patch, MagicMock
from m import read_in_range

class TestReadInRange(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_in_range(self, mock_read_csv):
        # Mock the data returned by pd.read_csv
        mock_df = pd.DataFrame({'order_id': [1, 2], 'amount': [100, 200]})
        mock_read_csv.return_value = mock_df
        
        # Call the function with a specific date range
        result = read_in_range(1, 2023, 3, 2023)
        
        # Check that pd.read_csv was called the correct number of times
        self.assertEqual(mock_read_csv.call_count, 3)
        
        # Check that the result is a concatenated DataFrame
        expected_df = pd.concat([mock_df, mock_df, mock_df], ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)

if __name__ == '__main__':
    unittest.main()