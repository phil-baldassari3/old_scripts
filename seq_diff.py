import os
import itertools
import pandas as pd

directory = '/Users/philipbaldassari/desktop/seq_diff_test/'

data = {}
for file in os.listdir(directory):
    if file.endswith('.seq'):
        #opening and reading seq file
        data[file.split('.')[0]] = open(file, 'r').read()
        
    else:
        continue       

print(data.keys())
 

df = pd.DataFrame(columns = ["Locus", "totprop", "Aprop", "Tprop", "Cprop", "Gprop"])

site = 0

for locus in zip(data.get('a'), data.get('b'), data.get('c')):

    
    site += 1
    
    Acount = locus.count("A")
    Tcount = locus.count("T")
    Ccount = locus.count("C")
    Gcount = locus.count("G")
    
    bpcount = Acount+Tcount+Ccount+Gcount
   
    if bpcount == 0:
        bpcount += 1
    else:
        bpcount == bpcount
       
    Aprop = Acount/bpcount
    Tprop = Tcount/bpcount
    Cprop = Ccount/bpcount
    Gprop = Gcount/bpcount

    totprop = Aprop + Tprop + Cprop + Gprop
    
    df = df.append({'Locus' : site, 'totprop' : totprop, 'Aprop' : Aprop, 'Tprop' : Tprop, 'Cprop' : Cprop, 'Gprop' : Gprop}, 
                ignore_index = True)




df2 = pd.DataFrame(columns = ["Locus", "totprop2", "Aprop2", "Tprop2", "Cprop2", "Gprop2"])

site2 = 0

for locus in zip(data.get('d'), data.get('e'), data.get('f')):
    
    site2 += 1
    
    Acount2 = locus.count("A")
    Tcount2 = locus.count("T")
    Ccount2 = locus.count("C")
    Gcount2 = locus.count("G")
    
    bpcount2 = Acount2+Tcount2+Ccount2+Gcount2
  
    if bpcount2 == 0:
        bpcount2 += 1
    else:
        bpcount2 == bpcount2
       
    Aprop2 = Acount2/bpcount2
    Tprop2 = Tcount2/bpcount2
    Cprop2 = Ccount2/bpcount2
    Gprop2 = Gcount2/bpcount2

    totprop2 = Aprop2 + Tprop2 + Cprop2 + Gprop2
    
    df2 = df2.append({'Locus' : site2 ,'totprop2' : totprop2, 'Aprop2' : Aprop2, 'Tprop2' : Tprop2, 'Cprop2' : Cprop2, 'Gprop2' : Gprop2}, 
                ignore_index = True)


combined = pd.merge(df, df2, on='Locus')



combined['Adiff'] = abs(combined['Aprop'] - combined['Aprop2'])
combined['Tdiff'] = abs(combined['Tprop'] - combined['Tprop2'])
combined['Cdiff'] = abs(combined['Cprop'] - combined['Cprop2'])
combined['Gdiff'] = abs(combined['Gprop'] - combined['Gprop2'])

combined['diff_score'] = combined[["Adiff","Tdiff","Cdiff","Gdiff"]].max(axis=1)

ridofmissing1 = combined[combined.totprop !=0]
ridofmissing2 = ridofmissing1[ridofmissing1.totprop2 !=0]

filtered = ridofmissing2[ridofmissing2.diff_score !=0]

print(filtered)

