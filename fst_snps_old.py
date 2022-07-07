#Script to to estimate fst on each SNP after calling and filtering

#importing modules
import pandas as pd
import numpy as np

#setting directory
directory = "/Users/philipbaldassari/desktop/seq_diff_test/"

#open dataframe
aln = pd.read_csv('filtered_SNPs.csv')

#Pop1 vs. Pop2
pop1 = aln.filter(['Locus', 'sample_a', 'sample_b', 'sample_c'], axis=1)

pop1_2_tot = aln.filter(['Locus', 'sample_a', 'sample_b', 'sample_c', 'sample_d', 'sample_e', 'sample_f'], axis=1)

#recount bp and frequencies

##new dataframe for bp counts
counts = pd.DataFrame(columns = ["Acount", "Tcount", "Ccount", "Gcount"])

##iterating through aln dataframe and counting bps for counts dataframe by tuples
for row in pop1.itertuples():
                
        Acount = row.count("A")
        Tcount = row.count("T")
        Ccount = row.count("C")
        Gcount = row.count("G")
        
        counts = counts.append({'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}, 
                ignore_index = True)

##merging counts to aln dataframe by index
pop1 = pd.merge(pop1, counts, left_index=True, right_index=True)

##summing for total bp count
pop1["bpcount"] = pop1['Acount'] + pop1['Tcount'] + pop1['Ccount'] + pop1['Gcount']

##allele frqeuncies per nucleotide
pop1['Aprop'] = pop1['Acount']/pop1['bpcount']
pop1['Tprop'] = pop1['Tcount']/pop1['bpcount']
pop1['Cprop'] = pop1['Ccount']/pop1['bpcount']
pop1['Gprop'] = pop1['Gcount']/pop1['bpcount']

#recount bp and frequencies

##new dataframe for bp counts
counts2 = pd.DataFrame(columns = ["Acount", "Tcount", "Ccount", "Gcount"])

##iterating through aln dataframe and counting bps for counts dataframe by tuples
for row in pop1_2_tot.itertuples():
                
        Acount = row.count("A")
        Tcount = row.count("T")
        Ccount = row.count("C")
        Gcount = row.count("G")
        
        counts2 = counts2.append({'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}, 
                ignore_index = True)

##merging counts to aln dataframe by index
pop1_2_tot = pd.merge(pop1_2_tot, counts2, left_index=True, right_index=True)

##summing for total bp count
pop1_2_tot["bpcount"] = pop1_2_tot['Acount'] + pop1_2_tot['Tcount'] + pop1_2_tot['Ccount'] + pop1_2_tot['Gcount']

##allele frqeuncies per nucleotide
pop1_2_tot['Aprop'] = pop1_2_tot['Acount']/pop1_2_tot['bpcount']
pop1_2_tot['Tprop'] = pop1_2_tot['Tcount']/pop1_2_tot['bpcount']
pop1_2_tot['Cprop'] = pop1_2_tot['Ccount']/pop1_2_tot['bpcount']
pop1_2_tot['Gprop'] = pop1_2_tot['Gcount']/pop1_2_tot['bpcount']


#Estimating Heterozygousity Pop1
aln['Hpop1'] = 1 - ((pop1['Aprop']**2) + (pop1['Tprop']**2) + (pop1['Cprop']**2) + (pop1['Gprop']**2))

#Estimating Heterozygousity Pop1 and 2
aln['Hpop1_2_tot'] = 1 - ((pop1_2_tot['Aprop']**2) + (pop1_2_tot['Tprop']**2) + (pop1_2_tot['Cprop']**2) + (pop1_2_tot['Gprop']**2))

#Fst Pop1 vs. Pop2
aln['Fst_Pop1_vs_Pop2'] = (aln['Hpop1_2_tot'] - aln['Hpop1'])/aln['Hpop1_2_tot']

#saving as csv
aln.to_csv('Fst_on_SNPs.csv', index=False)





