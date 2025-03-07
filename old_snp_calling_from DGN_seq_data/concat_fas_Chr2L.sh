#!/bin/bash

#setting working directory
cd /Users/philipbaldassari/Desktop/zim-cos_Chr2L

#alphabetizing the chunk list files
for file in *.txt
do
	sort $file -o $file
done

echo "Done sorting list files alphbetically"

#concatenating the individaul fasta files
for file in *.txt
do
	xargs < $file cat > zim-cos_Chr2L_$file.fa
done

echo "Done concatenating individual fasta files"

#removing individual fasta files
for fas in *.fas
do
	rm $fas
done

echo "Done removing individual files"
echo "Done!"

