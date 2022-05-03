#Unit Test case #1 to check if the path is correct and the initial count from the files are correct
from combine_csv import check_path, data_frame

import unittest 


class TestPath(unittest.TestCase):
    
    #validating if the path exists or not
    def test_path(self):
        result=check_path()
        self.assertEqual(result, "C:\\Users\\skmah\\Downloads\\Engineering Test Risk Analytics\\Engineering Test Risk Analytics\\Engineering Test Files\\")
    
    def test_count(self):
        self.assertEqual(data_frame(), 10)

if  __name__=='__main__':
    unittest.main()
    
    
    