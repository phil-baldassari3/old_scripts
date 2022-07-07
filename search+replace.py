#used to find and replace very large files
#place in directory with file.  The script reads the file, searched and replaces the character and reprints the whole file with the replacement

# Read in the file
with open('file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('old', 'new')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)


