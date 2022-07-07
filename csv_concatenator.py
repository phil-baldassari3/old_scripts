#importing modules
import pandas as pd
import glob
import os

#setting directory
directory = "/Users/philipbaldassari/desktop/fst_test/"
  
#merging the files
joined_files = os.path.join(directory, "SNPs_called_*.csv")
  
#list of all joined files
joined_list = glob.glob(joined_files)
  
#joinging files
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

#sort by locus
df = df.sort_values(["Locus"], ascending=True)

#saving as csv
df.to_csv('SNPs_called.csv', index=False)

print('Done!')





