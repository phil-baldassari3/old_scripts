#script to loop through folder and convert all .seq files to a fasta format in a new folder
#put this script file in the directory with the seq files

import os,sys

#set directories
seq_directory = #path/to/directory/ <-- make sure it ends with a '/'

converted_fas_dir = #path/to/directory/ <-- make sure it ends with a '/'



#converting the seq files to new files in fasta format
for file in os.listdir(seq_directory):
    if file.endswith('.seq'):
        #opening and reading seq file
        seq_file = open(file)
        sequence = seq_file.read()
        #creating new file with header and sequence
        with open('{path}'.format(path = converted_fas_dir) + '{file}'.format(file = file), 'w') as conversion:
            conversion.write('>' + '{filename}'.format(filename = file.split('_')[0]) + '\n' + sequence + '\n')
    else:
        continue       


     
#change file extention to fasta
for f in os.listdir(converted_fas_dir):
    if f.endswith('.seq'):
        infilename = os.path.join(converted_fas_dir,f)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(f)
        newname = infilename.replace('.seq', '.fas')
        output = os.rename(infilename, newname)
    else:
        continue
   
'''
#old code: used to clean the " + " from the beginning of the converted files when creation line read "{path} + {file}"
#for cleaning off the '+ ' from the creation of the new files
for file in os.listdir(converted_fas_dir):
    if file.endswith('.fas'):
        infilename = os.path.join(converted_fas_dir,file)
        if not os.path.isfile(infilename): continue
        oldname = os.path.splitext(f)
        newname = infilename.replace(' + ', '')
        output = os.rename(infilename, newname)
    else:
        continue

'''
