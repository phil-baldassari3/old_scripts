#script to replace the r5 coordnates with r6 coordinates in the csv files

#importing modules
import os,sys
import pandas as pd
import numpy as np
from multiprocessing import Pool

#setting directory
directory = "/Users/philipbaldassari/Desktop/zim_cos_fst_data"
os.chdir(directory)


#get list of txt list files for parallel pool mapping
file_list = []

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_list.append(file)
    else:
        continue

print(file_list)
print('\n\n')


def coordinate_switcher(infile):

    #opening dataframe
    df = pd.read_csv(infile)

    print("opened ", infile)

    df.drop('Site', axis=1, inplace=True)

    print("dropped r5 sites from ", infile)

    for file in os.listdir(directory):
        if file.endswith('.txt') and infile.split('.')[0] in file:
            #opening the coordinate file
            coordinate_file = open(file, "r")
  
            #reading the file
            coordinate_data = coordinate_file.read()
  
            #coordinates to list
            coordinates = coordinate_data.split("\n")

            coordinate_file.close()

            break
            
        else:
            continue

    #coordinate cleaning
    coordinates = [i.replace('X:', '') for i in coordinates]
    coordinates = [i.replace('2L:', '') for i in coordinates]
    coordinates = [i.replace('2R:', '') for i in coordinates]
    coordinates = [i.replace('3L:', '') for i in coordinates]
    coordinates = [i.replace('3R:', '') for i in coordinates]

    #adding column
    df['r6_site'] = pd.Series(coordinates)

    col_list = list(df.columns)

    col_list.insert(1, col_list.pop(-1))

    df = df[col_list]

    print("inserted r6 sites in ", infile)

    #saving as csv
    df.to_csv("r6_" + infile, index=False)

    print("saved ", "r6_" + infile)


#for parallele mapping

#run in parallel
def run_in_parallel():
    pool = Pool(processes=18)
    pool.map(coordinate_switcher, file_list)


if __name__ == '__main__':
    run_in_parallel()


