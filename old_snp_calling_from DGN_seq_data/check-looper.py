#I recommend running this from IDLE and not terminal
#This is just to check things quickly in all the files at once
#put this script into the directory with the files you are looping through

import os

directory = #path/to/directory

'''
#checking the length of each file
#length should be...
for file in os.listdir(directory):
    if file.endswith('.seq'):
        file_open = open(file)
        file_read = file_open.read()
        length = len(file_read)
        print(file, '\n', '---------------> ', length)
    else:
        continue
'''

#checking for files of different length
print('wait for it to load; this loop takes a long time.')
print('if a file prints, its a different length.')
print('if nothing prints, all files are the same length')
for file in os.listdir(directory):
    if file.endswith('.seq'):
        file_open = open(file)
        file_read = file_open.read()
        length = len(file_read)
        if length != #how long should it be?:
            print(file)
        else:
            continue
    

#prints portions of each file where you tell it to
def find_info_loci(index1, index2):
    for file in os.listdir(directory):
        if file.endswith('.seq'):
          file_open = open(file)
          file_read = file_open.read()
          print(file, '\n', '------------------->', file_read[index1: index2])
        else:
            continue
