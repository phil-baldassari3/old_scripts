#script to create chunked fasta alignment flies from the seq files

import os,sys

#set directories
seq_directory ='/Users/philipbaldassari/desktop/zim-cos_Chr2Lseq/'

converted_fas_dir ='/Users/philipbaldassari/desktop/zim-cos_Chr2L/'

#getting length of sequence
seq = open('FR2N_Chr2L.seq')
seq_data = seq.read()
seqlen = len(seq_data)
seq.close()


#set window size
win = 200000

#counter for loop
counter = 0

os.chdir(seq_directory)

#setting window with range function
for i in range(0, seqlen, win):
    j = seqlen if i+win>seqlen else i+win


    #converting the seq files to new files in fasta format
    for file in os.listdir(seq_directory):
        if file.endswith('.seq'):
            #opening and reading seq file
            seq_file = open(file)
            sequence = seq_file.read()
            #creating new file with header and sequence
            with open('{path}'.format(path = converted_fas_dir) + '{file}'.format(file = file), 'w') as conversion:
                conversion.write('>' + '{filename}'.format(filename = file.split('_')[0]) + '\n' + sequence[i:j] + '\n')
        else:
            continue


    #change file extention to fasta
    for f in os.listdir(converted_fas_dir):
        if f.endswith('.seq'):
            infilename = os.path.join(converted_fas_dir,f)
            if not os.path.isfile(infilename): continue
            oldbase = os.path.splitext(f)
            newname = infilename.replace('.seq', '_{num}.fas'.format(num=counter))
            output = os.rename(infilename, newname)
        else:
            continue

    #updating the counter
    counter += 1

#count for number of files created
count = 0

#find number of files
for file in os.listdir(converted_fas_dir):
    if file.endswith('.fas'):
        count +=1
    else:
        continue

#setting number of fasta files
num_of_fas = count

#changing working directory
os.chdir(converted_fas_dir)

#range from 0 to number of chunks
for i in range(int(num_of_fas/619)):

    #making a file with list of individual files per chunk
    with open('chunk{num}.txt'.format(num=i), 'a') as list_file:

        #appending name of file to the link of the chunk of that file
        for file in os.listdir(converted_fas_dir):
            if file.endswith('_{num}.fas'.format(num=i)):
                list_file.write(file + '\n')
	    else:
                continue

print('Done!')
print('Run concat_fas_Chr2L.sh in this directory to complete the concatenation process.')


