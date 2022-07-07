#second version of seq_diff script.

#importing modules
import os
import itertools
import pandas as pd
import numpy as np

#setting directory
directory = '/Users/philipbaldassari/desktop/seq_diff_test/'

#extracting data
data = {}
for file in os.listdir(directory):
    if file.endswith('.seq'):
        #opening and reading seq file
        data[file.split('.')[0]] = open(file, 'r').read()
        
    else:
        continue       

print(data.keys())

#pop1
df = pd.DataFrame(columns = ["Locus", "Acount", "Tcount", "Ccount", "Gcount"])

site = 0

for locus in zip(data.get('a'), data.get('b'), data.get('c')):

    
    site += 1
    
    Acount = locus.count("A")
    Tcount = locus.count("T")
    Ccount = locus.count("C")
    Gcount = locus.count("G")
	
    df = df.append({'Locus' : site, 'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}, 
                ignore_index = True)
				

#Pop2
df2 = pd.DataFrame(columns = ["Locus", "Acount2", "Tcount2", "Ccount2", "Gcount2"])

site2 = 0

for locus2 in zip(data.get('d'), data.get('e'), data.get('f')):

    
    site2 += 1
    
    Acount2 = locus2.count("A")
    Tcount2 = locus2.count("T")
    Ccount2 = locus2.count("C")
    Gcount2 = locus2.count("G")
	
    df2 = df2.append({'Locus' : site2, 'Acount2' : Acount2, 'Tcount2' : Tcount2, 'Ccount2' : Ccount2, 'Gcount2' : Gcount2}, 
                ignore_index = True)


#merge on locus (all loci present)
combined = pd.merge(df, df2, on='Locus')

#calculations

#bpcounts
combined['bpcount'] = combined['Acount'] + combined['Tcount'] + combined['Ccount'] + combined['Gcount']
combined['bpcount2'] = combined['Acount2'] + combined['Tcount2'] + combined['Ccount2'] + combined['Gcount2']

combined['bpcount'] = combined['bpcount'].replace([0], np.nan)
combined['bpcount2'] = combined['bpcount2'].replace([0], np.nan)

print(combined)
#divisions

combined['Aprop'] = combined['Acount']/combined['bpcount']
combined['Tprop'] = combined['Tcount']/combined['bpcount']
combined['Cprop'] = combined['Ccount']/combined['bpcount']
combined['Gprop'] = combined['Gcount']/combined['bpcount']

combined['Aprop2'] = combined['Acount2']/combined['bpcount2']
combined['Tprop2'] = combined['Tcount2']/combined['bpcount2']
combined['Cprop2'] = combined['Ccount2']/combined['bpcount2']
combined['Gprop2'] = combined['Gcount2']/combined['bpcount2']

#difference scoring
combined['Adiff'] = abs(combined['Aprop'] - combined['Aprop2'])
combined['Tdiff'] = abs(combined['Tprop'] - combined['Tprop2'])
combined['Cdiff'] = abs(combined['Cprop'] - combined['Cprop2'])
combined['Gdiff'] = abs(combined['Gprop'] - combined['Gprop2'])

combined['diff_score'] = combined[["Adiff","Tdiff","Cdiff","Gdiff"]].max(axis=1)


#filter out monomorphic sites
filtered = combined[combined['diff_score'].notna() & combined.diff_score != 0]

print(filtered)

filtered.to_csv('seq_diff_test2.csv', index=False)










