# TEST CASE for Blank.csv// count should be 20 as there is no data in the file

import csv , sys, os
header = ['Source IP', 'Count', 'Events per Second']
path=input("Please input your path:")
if path=='' or os.path.exists==False:
    print("Wrong file or file path")
    sys.exit()
else:
    pass
content3 = []
    
    
with open(path+'Blank.csv', 'w', encoding='UTF8', newline='') as file3:
    writer = csv.writer(file3)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(content3)
##################################

from combine_csv import check_path, data_frame

import unittest 


class TestPath(unittest.TestCase):
   
        # validating if the count from initial files are correct
    def test_count(self):
        self.assertEqual(data_frame(), 20)


if  __name__=='__main__':
    unittest.main()