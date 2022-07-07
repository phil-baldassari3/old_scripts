#importing modules
import os
import pandas as pd
import numpy as np

#setting directory
directory = '/Users/philipbaldassari/desktop/seq_diff_test/'


#making aln dataframe
aln = pd.DataFrame()


for file in os.listdir(directory):
    if file.endswith('.seq'):
        seq_file = open(file)
        sequence = seq_file.read()
        listseq = list(sequence)
        aln[file.split('.')[0]] = listseq
    else:
        continue

aln = aln.replace('N', np.nan)
aln = aln.replace('A', 1)
aln = aln.replace('T', 2)
aln = aln.replace('C', 3)
aln = aln.replace('G', 4)

aln['sum'] = aln.sum(axis=1)
aln['totbp'] = aln.count(axis='columns') - 1
aln['check'] = aln['sum']/aln['totbp']

aln['locus'] = aln.index + 1

aln = aln[aln['check'] != 1]
aln = aln[aln['check'] != 2]
aln = aln[aln['check'] != 3]
aln = aln[aln['check'] != 4]

print(aln)
