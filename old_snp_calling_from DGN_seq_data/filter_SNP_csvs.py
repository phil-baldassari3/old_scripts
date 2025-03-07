#Script to filter out singletons and triallelic snps

#importing modules
import os,sys
import pandas as pd
import numpy as np
from multiprocessing import Pool

#setting directory
directory = "/Users/philipbaldassari/Desktop/zim-cos_ChrX"

'''
#get list of csvs for parallel pool mapping
file_list = []

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_list.append(file)
    else:
        continue

print(file_list)
'''

#filtering and overwriting
def filter(infile):

    #open dataframe
    df = pd.read_csv(infile)

    #replace singletons with 'N'
    df.loc[df['Acount'] == 1] = df.replace('A', 'N')
    df.loc[df['Tcount'] == 1] = df.replace('T', 'N')
    df.loc[df['Ccount'] == 1] = df.replace('C', 'N')
    df.loc[df['Gcount'] == 1] = df.replace('G', 'N')

    print("singletons replaced with 'N' in " + infile)

    df = df.drop(['Acount', 'Tcount', 'Ccount', 'Gcount', 'bpcount', 'Aprop', 'Tprop', 'Cprop', 'Gprop', 'MajorAF'], axis=1)

    #recount bp and frequencies
    #iterating through df dataframe and counting bps for counts dataframe by tuples
    Acount = []
    Tcount = []
    Ccount = []
    Gcount = []

    for row in df.itertuples():
        
        Acount.append(row.count("A"))
        Tcount.append(row.count("T"))
        Ccount.append(row.count("C"))
        Gcount.append(row.count("G"))
	
    dict_counts = {'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}

    counts = pd.DataFrame.from_dict(dict_counts)

    #merging counts to df dataframe by index
    df = pd.merge(df, counts, left_index=True, right_index=True)

    del counts

    print("allele counts recounted for " + infile)

    ##summing for total bp count
    df["bpcount"] = df['Acount'] + df['Tcount'] + df['Ccount'] + df['Gcount']

    ##allele frqeuncies per nucleotide
    df['Aprop'] = df['Acount']/df['bpcount']
    df['Tprop'] = df['Tcount']/df['bpcount']
    df['Cprop'] = df['Ccount']/df['bpcount']
    df['Gprop'] = df['Gcount']/df['bpcount']

    ##Major allele Frequency
    df['MajorAF'] = df[["Aprop","Tprop","Cprop","Gprop"]].max(axis=1)

    #getting rid of monomorphic sites (may have been replaced singletons)
    df = df[df.MajorAF !=1]

    print("allele frequencies recounted for " + infile + " and monomorphic sites removed")

    #remove triallelic SNPs
    df = df.drop(df[~((df.Acount == 0) & (df.Tcount == 0) | (df.Acount == 0) & (df.Ccount == 0) | (df.Acount == 0) & (df.Gcount == 0) | (df.Tcount == 0) & (df.Ccount == 0) | (df.Tcount == 0) & (df.Gcount == 0) | (df.Ccount == 0) & (df.Gcount == 0))].index)

    print("trialleleic sites removed for " + infile)
'''
    #overwriting csv
    with open(infile, "w") as csv_file:

        df.to_csv(csv_file, index=False)

    print("############################################" + "\n" + infile + " overwritten with filtered dataframe" + "\n" + "############################################")
'''
        
#for parallele mapping
csv_list = []

#run in parallel
def run_in_parallel():
    pool = Pool(processes=8)
    pool.map(filter, csv_list)


if __name__ == '__main__':
    run_in_parallel()
