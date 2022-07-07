#Script to filter out singletons, maf, and triallelic snps

#importing modules
import pandas as pd
import numpy as np

#setting directory
directory = "/Users/philipbaldassari/desktop/seq_diff_test/"

#open dataframe
aln = pd.read_csv('SNPs_called.csv')

#remove singletons
aln.loc[aln['Acount'] == 1] = aln.replace('A', np.nan)
aln.loc[aln['Tcount'] == 1] = aln.replace('T', np.nan)
aln.loc[aln['Ccount'] == 1] = aln.replace('C', np.nan)
aln.loc[aln['Gcount'] == 1] = aln.replace('G', np.nan)

aln = aln.drop(['Acount', 'Tcount', 'Ccount', 'Gcount', 'bpcount', 'Aprop', 'Tprop', 'Cprop', 'Gprop', 'MajorAF'], axis=1)

#recount bp and frequencies

##new dataframe for bp counts
counts = pd.DataFrame(columns = ["Acount", "Tcount", "Ccount", "Gcount"])

##iterating through aln dataframe and counting bps for counts dataframe by tuples
for row in aln.itertuples():
                
        Acount = row.count("A")
        Tcount = row.count("T")
        Ccount = row.count("C")
        Gcount = row.count("G")
        
        counts = counts.append({'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}, 
                ignore_index = True)

##merging counts to aln dataframe by index
aln = pd.merge(aln, counts, left_index=True, right_index=True)

##summing for total bp count
aln["bpcount"] = aln['Acount'] + aln['Tcount'] + aln['Ccount'] + aln['Gcount']

##allele frqeuncies per nucleotide
aln['Aprop'] = aln['Acount']/aln['bpcount']
aln['Tprop'] = aln['Tcount']/aln['bpcount']
aln['Cprop'] = aln['Ccount']/aln['bpcount']
aln['Gprop'] = aln['Gcount']/aln['bpcount']

##Major allele Frequency
aln['MajorAF'] = aln[["Aprop","Tprop","Cprop","Gprop"]].max(axis=1)

#maf (5%)
aln = aln[aln.MajorAF <=0.95]

#remove triallelic SNPs
aln = aln.drop(aln[~((aln.Acount == 0) & (aln.Tcount == 0) | (aln.Acount == 0) & (aln.Ccount == 0) | (aln.Acount == 0) & (aln.Gcount == 0) | (aln.Tcount == 0) & (aln.Ccount == 0) | (aln.Tcount == 0) & (aln.Gcount == 0) | (aln.Ccount == 0) & (aln.Gcount == 0))].index)

#saving as csv
aln.to_csv('filtered_SNPs.csv', index=False)

