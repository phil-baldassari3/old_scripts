#script to loop through seq folder and create a pop.txt file that contains the population ID for each fly.
#The nature of the for loop is not alphbetical so you will need to sort to a new file in terminal
#Put this script in directory with the seq files

import os
import re


#set directories
seq_directory = '/Users/philipbaldassari/Desktop/zim-cos_ChrXseq/'

vcf_directory = '/Users/philipbaldassari/Desktop/'


#creating pop.txt file, printing in sample IDs by splitting file names at '_'
with open('{path}'.format(path = vcf_directory) + 'unsorted_pop.txt', 'w') as pop:
        for file in os.listdir(seq_directory):
                if file.endswith('.seq'):
                        pop.write('{filename}'.format(filename = file.split('_')[0]) + '\n')
                else:
                        continue       


