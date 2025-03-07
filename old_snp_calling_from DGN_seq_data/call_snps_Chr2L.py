#3rd iteration of the python based SNP calling tool.  Goal is to make an alignment dataframe and filter out the monomorphic sites.

#importing modules
import os,sys
import pandas as pd
import numpy as np
import time
from multiprocessing import Pool


start = time.time()



#setting directory
directory = "/Users/philipbaldassari/Desktop/zim-cos_Chr2L"
'''
file_list = []

for file in os.listdir(directory):
    if file.endswith('.fa'):
	file_list.append(file)
    else:
	continue



print("file list completed. used for multiprocessing")
'''

def fasta2df(infile):
    with open(infile, "r") as fasta_file:
        fasta = {line.strip(">\n"):next(fasta_file).rstrip() for line in fasta_file}

	#converting values in dictionary to list
        for k, v in fasta.items():
            fasta[k] = list(v)

    del fasta_file

    #making dataframe from dictionary
    aln = pd.DataFrame.from_dict(fasta)

    del fasta


    #Add Locus column
    aln.insert(0, "Locus", aln.index + 1 + ((int(infile.split("_")[3]))*200000))


    #iterating through aln dataframe and counting bps for counts dataframe by tuples
    Acount = []
    Tcount = []
    Ccount = []
    Gcount = []

    for row in aln.itertuples():
        Acount.append(row.count("A"))
        Tcount.append(row.count("T"))
        Ccount.append(row.count("C"))
        Gcount.append(row.count("G"))

    dict_counts = {'Acount' : Acount, 'Tcount' : Tcount, 'Ccount' : Ccount, 'Gcount' : Gcount}

    counts = pd.DataFrame.from_dict(dict_counts)

    
    #merging counts to aln dataframe by index
    aln = pd.merge(aln, counts, left_index=True, right_index=True)

    del counts

    print('done...continuing')
    print('estimating allele frequecies at each site...')

    #summing for total bp count
    aln["bpcount"] = aln['Acount'] + aln['Tcount'] + aln['Ccount'] + aln['Gcount']

    #getting rid of rows with zero bps
    aln = aln[aln.bpcount !=0]

    #allele frqeuncies per nucleotide
    aln['Aprop'] = aln['Acount']/aln['bpcount']
    aln['Tprop'] = aln['Tcount']/aln['bpcount']
    aln['Cprop'] = aln['Ccount']/aln['bpcount']
    aln['Gprop'] = aln['Gcount']/aln['bpcount']

    #Major allele Frequency
    aln['MajorAF'] = aln[["Aprop","Tprop","Cprop","Gprop"]].max(axis=1)

    print('done...continuing')
    print('getting rid of monomorphic sites...')

    #getting rid of monomorphic sites
    aln = aln[aln.MajorAF !=1]

    print('done...finalizing')


    #saving as csv
    aln.to_csv('{file}_SNPs_called.csv'.format(file=infile), index=False)

    print('Process complete! A csv files has been saved to this directory named SNPs_called.csv{file}SNPs_called.csv'.format(file=infile))


file_list = ['zim-cos_Chr2L_chunk_17_.fa', 'zim-cos_Chr2L_chunk_16_.fa', 'zim-cos_Chr2L_chunk_28_.fa', 'zim-cos_Chr2L_chunk_14_.fa', 'zim-cos_Chr2L_chunk_15_.fa', 'zim-cos_Chr2L_chunk_29_.fa', 'zim-cos_Chr2L_chunk_11_.fa', 'zim-cos_Chr2L_chunk_39_.fa', 'zim-cos_Chr2L_chunk_38_.fa', 'zim-cos_Chr2L_chunk_10_.fa', 'zim-cos_Chr2L_chunk_12_.fa', 'zim-cos_Chr2L_chunk_13_.fa', 'zim-cos_Chr2L_chunk_48_.fa', 'zim-cos_Chr2L_chunk_60_.fa', 'zim-cos_Chr2L_chunk_0_.fa', 'zim-cos_Chr2L_chunk_74_.fa', 'zim-cos_Chr2L_chunk_111_.fa', 'zim-cos_Chr2L_chunk_105_.fa', 'zim-cos_Chr2L_chunk_104_.fa', 'zim-cos_Chr2L_chunk_110_.fa', 'zim-cos_Chr2L_chunk_75_.fa', 'zim-cos_Chr2L_chunk_61_.fa', 'zim-cos_Chr2L_chunk_1_.fa', 'zim-cos_Chr2L_chunk_49_.fa', 'zim-cos_Chr2L_chunk_77_.fa', 'zim-cos_Chr2L_chunk_3_.fa', 'zim-cos_Chr2L_chunk_63_.fa', 'zim-cos_Chr2L_chunk_88_.fa', 'zim-cos_Chr2L_chunk_106_.fa', 'zim-cos_Chr2L_chunk_112_.fa', 'zim-cos_Chr2L_chunk_113_.fa', 'zim-cos_Chr2L_chunk_107_.fa', 'zim-cos_Chr2L_chunk_89_.fa', 'zim-cos_Chr2L_chunk_2_.fa', 'zim-cos_Chr2L_chunk_62_.fa', 'zim-cos_Chr2L_chunk_76_.fa', 'zim-cos_Chr2L_chunk_72_.fa', 'zim-cos_Chr2L_chunk_66_.fa', 'zim-cos_Chr2L_chunk_6_.fa', 'zim-cos_Chr2L_chunk_99_.fa', 'zim-cos_Chr2L_chunk_103_.fa', 'zim-cos_Chr2L_chunk_102_.fa', 'zim-cos_Chr2L_chunk_98_.fa', 'zim-cos_Chr2L_chunk_67_.fa', 'zim-cos_Chr2L_chunk_7_.fa', 'zim-cos_Chr2L_chunk_73_.fa', 'zim-cos_Chr2L_chunk_5_.fa', 'zim-cos_Chr2L_chunk_65_.fa', 'zim-cos_Chr2L_chunk_71_.fa', 'zim-cos_Chr2L_chunk_59_.fa', 'zim-cos_Chr2L_chunk_114_.fa', 'zim-cos_Chr2L_chunk_100_.fa', 'zim-cos_Chr2L_chunk_101_.fa', 'zim-cos_Chr2L_chunk_115_.fa', 'zim-cos_Chr2L_chunk_58_.fa', 'zim-cos_Chr2L_chunk_70_.fa', 'zim-cos_Chr2L_chunk_4_.fa', 'zim-cos_Chr2L_chunk_64_.fa', 'zim-cos_Chr2L_chunk_9_.fa', 'zim-cos_Chr2L_chunk_69_.fa', 'zim-cos_Chr2L_chunk_41_.fa', 'zim-cos_Chr2L_chunk_55_.fa', 'zim-cos_Chr2L_chunk_82_.fa', 'zim-cos_Chr2L_chunk_96_.fa', 'zim-cos_Chr2L_chunk_97_.fa', 'zim-cos_Chr2L_chunk_83_.fa', 'zim-cos_Chr2L_chunk_54_.fa', 'zim-cos_Chr2L_chunk_40_.fa', 'zim-cos_Chr2L_chunk_8_.fa', 'zim-cos_Chr2L_chunk_68_.fa', 'zim-cos_Chr2L_chunk_56_.fa', 'zim-cos_Chr2L_chunk_42_.fa', 'zim-cos_Chr2L_chunk_95_.fa', 'zim-cos_Chr2L_chunk_81_.fa', 'zim-cos_Chr2L_chunk_80_.fa', 'zim-cos_Chr2L_chunk_94_.fa', 'zim-cos_Chr2L_chunk_43_.fa', 'zim-cos_Chr2L_chunk_57_.fa', 'zim-cos_Chr2L_chunk_53_.fa', 'zim-cos_Chr2L_chunk_47_.fa', 'zim-cos_Chr2L_chunk_90_.fa', 'zim-cos_Chr2L_chunk_84_.fa', 'zim-cos_Chr2L_chunk_85_.fa', 'zim-cos_Chr2L_chunk_91_.fa', 'zim-cos_Chr2L_chunk_46_.fa', 'zim-cos_Chr2L_chunk_52_.fa', 'zim-cos_Chr2L_chunk_44_.fa', 'zim-cos_Chr2L_chunk_50_.fa', 'zim-cos_Chr2L_chunk_78_.fa', 'zim-cos_Chr2L_chunk_87_.fa', 'zim-cos_Chr2L_chunk_93_.fa', 'zim-cos_Chr2L_chunk_109_.fa', 'zim-cos_Chr2L_chunk_108_.fa', 'zim-cos_Chr2L_chunk_92_.fa', 'zim-cos_Chr2L_chunk_86_.fa', 'zim-cos_Chr2L_chunk_79_.fa', 'zim-cos_Chr2L_chunk_51_.fa', 'zim-cos_Chr2L_chunk_45_.fa', 'zim-cos_Chr2L_chunk_22_.fa', 'zim-cos_Chr2L_chunk_36_.fa', 'zim-cos_Chr2L_chunk_37_.fa', 'zim-cos_Chr2L_chunk_23_.fa', 'zim-cos_Chr2L_chunk_35_.fa', 'zim-cos_Chr2L_chunk_21_.fa', 'zim-cos_Chr2L_chunk_20_.fa', 'zim-cos_Chr2L_chunk_34_.fa', 'zim-cos_Chr2L_chunk_30_.fa', 'zim-cos_Chr2L_chunk_24_.fa', 'zim-cos_Chr2L_chunk_18_.fa', 'zim-cos_Chr2L_chunk_19_.fa', 'zim-cos_Chr2L_chunk_25_.fa', 'zim-cos_Chr2L_chunk_31_.fa', 'zim-cos_Chr2L_chunk_27_.fa', 'zim-cos_Chr2L_chunk_33_.fa', 'zim-cos_Chr2L_chunk_32_.fa', 'zim-cos_Chr2L_chunk_26_.fa']

#run in parallel
def run_in_parallel():
    pool = Pool(processes=10)
    pool.map(fasta2df, file_list)


if __name__ == '__main__':
    run_in_parallel()




end = time.time()





print("\n\n\n\nRUNTIME:", (end-start), "s")









