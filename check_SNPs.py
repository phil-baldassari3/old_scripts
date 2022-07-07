#put this script in directory with files you are looping through

import os

directory = #path/to/directory


'''
for file in os.listdir(directory):
    print(file)
'''

def find_info_loci(index1, index2):
    for file in os.listdir(directory):
        if file.endswith('.seq'):
          file_open = open(file)
          file_read = file_open.read()
          print(file, '\n', '------------------->', file_read[index1: index2])
        else:
            continue




#find_info_loci(19112000, 19112315)



