#script to scrape flybase coordinates from csv files. first step in r5 to r6 coordinate conversion process. to be used with r5_to_r6_coordinate_converter.sh

#importing modules
import os,sys
import pandas as pd
import numpy as np
from multiprocessing import Pool

#setting directory
directory = "/Users/philipbaldassari/Desktop/zim_cos_fst_data"


#get list of csvs for parallel pool mapping
file_list = []

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_list.append(file)
    else:
        continue

print(file_list)
print("\n")


#scraper function
def r5_coordinate_scraper(infile):


    print("python: opening ", infile)

    #reading csv
    df = pd.read_csv(infile)

    #extracting coordinates
    coord = df.filter(["Chrom", "Site"], axis=1)

    #setting new file name
    txt_filename = "r5_{csv_filename}.txt".format(csv_filename = infile.split('.')[0])

    #saving txt file
    coord.to_csv(txt_filename, header=None, index=None)

    print("python: coordinates from ", infile, " saved to txt file. formatting now...")

    #formatting txt file
    with open(txt_filename, 'r') as file :
        filedata = file.read()

    #formatting
    filedata = filedata.replace('"', '')
    filedata = filedata.replace(',', ':')
    filedata = filedata.replace('\n', '\n' + '\n')

    #overwriting file
    with open(txt_filename, 'w') as f:
        f.write(filedata)

    print("python: done scraping from ", infile)




#for parallel mapping

#run in parallel
def run_in_parallel():
    pool = Pool(processes=18)
    pool.map(r5_coordinate_scraper, file_list)


if __name__ == '__main__':
    run_in_parallel()


