# TEST CASE for NA PREVIEW.csv// count should be now 20 as there are 5 new rows

import csv , sys, os
header = ['Source IP', 'Count', 'Events per Second']
path=input("Please input your path:")
if path=='' or os.path.exists==False:
    print("Wrong file or file path")
    sys.exit()
else:
    pass
content2 = [
    ['44.22.11.23', 28748, 200],
    ['14.2.3.4', 2381741, 3232],
    ['16.2.1.3', 199, 4342],
    ['26.1.3.5', 468, 2323],
    ['45.3.24.3', 1246700, 1]
]
    
    
with open(path+'NA Preview.csv', 'w', encoding='UTF8', newline='') as file2:
    writer = csv.writer(file2)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(content2)

 # create a blank file with headers only for test 3: This files should not be added to the combined.csv  
    


from combine_csv import check_path, data_frame

import unittest 


class TestPath(unittest.TestCase):
   
        # validating if the count from initial files are correct
    def test_count(self):
        self.assertEqual(data_frame(), 20)


if  __name__=='__main__':
    unittest.main()