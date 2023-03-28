#importing modules
import io
import os

#setting directory
directory = '/Users/philipbaldassari/Desktop/txt_fixer'

#loops through directory to find only .txt files
for file in os.listdir(directory):
    if file.endswith('.txt'):

        #opening vcf file as open file
        with open(file, 'r') as open_file:
            data = open_file.read()

            data = data.replace('\n', ', ')
            

        #writing new file
        with open(file, 'w') as fixed_file:
            fixed_file.write(data)

            


