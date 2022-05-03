#Unit Test case #2 to check Prod 4.csv and count should be 15 as there are 5 new rows
import csv , sys, os
header = ['Source IP', 'Count', 'Events per Second']
content = [
    ['22.22.11.23', 28748, 200],
    ['1.2.3.4', 2381741, 3232],
    ['11.2.1.3', 199, 4342],
    ['2.1.3.5', 468, 2323],
    ['5.3.24.3', 1246700, 1]
]

# create file Asia Prod 4 for the test case 1: 

path=input("Please input your path:")
if path=='' or os.path.exists==False:
    print("Wrong file or file path")
    sys.exit()
else:
    pass
with open(path+'Asia Prod 4.csv', 'w', encoding='UTF8', newline='') as file1:
    writer = csv.writer(file1)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(content)

from combine_csv import check_path, data_frame

import unittest 


class TestPath(unittest.TestCase):
   
        # validating if the count from initial files are correct
    def test_count(self):
        self.assertEqual(data_frame(), 15)


if  __name__=='__main__':
    unittest.main()