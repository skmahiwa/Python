# import glob, pandas and os libraries -- V2
from glob import glob
import pandas as pd
import os.path
import sys
# an empty list to hold data from multiple csv files using pandas dataframes
dataframe_list=[]

#####function to check invalid path and define the file storage path ##########
def check_path():
    path=input("Please input your path:")
    if path=='' or os.path.exists(path)==False:
        print("Wrong file or file path")
        sys.exit()
    else:
        pass
    return path

########################End of Function#####################################
path=check_path()

# only pick csv files
file_type='*.csv'

source_path=path+file_type

###################Function to creat data_frame from csv files#########################################

def data_frame():
    # Iterate through each file available in your directory folder
    for filename in glob(source_path):
        if filename=='Combined.csv':
            pass
        else:
            data_frame1 = pd.read_csv(filename)
        
            #removing space from beginning of the file name and removing numbers, spaces and special characters from the end of file name
            env_name = os.path.basename(filename).lstrip('').rstrip(' 0123456789-_@#$%^&*?/\[]{}~().csv')
            data_frame1['Environment'] = env_name
            dataframe_list.append(data_frame1)
            # getting data from data frame list and removing duplicates based on Source IP column
        
    from os.path import exists
    file_exists = exists(path + 'Combined.csv')
    if file_exists==True:
        data_frame4=pd.read_csv(path + 'Combined.csv')
        dataframe_list.append(data_frame4)
    else:
        pass    
    data_frame2 = pd.concat(dataframe_list, axis=0, ignore_index=True).drop_duplicates(subset='Source IP', keep='last')

        # a new data frame (data_frame3) is created to only select two required columns ( Source IP and Environment)
    data_frame3=data_frame2[['Source IP', 'Environment']]

    data_frame3.to_csv(path + 'Combined.csv', mode='w', header=True, index=False)
    total_records=data_frame3['Source IP'].count()
    return total_records
total_count=data_frame()
print(total_count)
##########################End of function data_frame#########################################################################


# now move the processed files which are added to combined.csv to a new folder (Processed) and duplicate file to Bad Folder

import shutil
import datetime

# Create a destination folder for PROCESSED FILES and Bad_File Folder for duplicate files
dest_path = input('Please input path to your Processed File Folder : ')

bad_file_path=input('Please input path to your Bad/duplicate File Folder : ')

#use makedirs to create directories by date
os.makedirs(dest_path + datetime.datetime.now().strftime('%Y\%m\%d'), exist_ok=True)


#Move files to Processed and Bad folder using shutil

for filename in glob(source_path):
    f=os.path.basename(filename)
    if f=='Combined.csv':
        continue
    # if any duplicate file exists move it to bad file folder
    elif os.path.exists((dest_path + datetime.datetime.now().strftime("%Y/%m/%d"))+"/"+f):
        os.makedirs(bad_file_path + datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%p"), exist_ok=True)
        shutil.move(filename, bad_file_path + datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%p") )
       
    else:
        shutil.move(filename, (dest_path + datetime.datetime.now().strftime("%Y/%m/%d")) )
        shutil.SameFileError
        
# print how many duplicate files are now moved to the Bad File folder
try: 
    badfile_dir=(bad_file_path + datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%p"))
    badcount=0
    for path in os.listdir(badfile_dir):
    # check if current path is a file
        if os.path.isfile(os.path.join(badfile_dir, path)):
            badcount += 1
    print('Bad File moved:', badcount) 
except Exception:
        print('No Bad File Found in this run')
