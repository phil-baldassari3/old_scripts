#!/bin/bash

echo "Preprocessing sequence data"

#Chrom X
cd /Users/philipbaldassari/Desktop/zim-cos_ChrXseq
python /Users/philipbaldassari/Desktop/zim-cos_ChrXseq/fas_chunks_ChrX.py

cd /Users/philipbaldassari/Desktop/zim-cos_ChrX
bash /Users/philipbaldassari/Desktop/zim-cos_ChrX/concat_fas_ChrX.sh

echo "################################################################################################"
echo "fasta alignment chunk files made for Chrom X...continuing to call SNPs to csv files."
echo "################################################################################################"

python /Users/philipbaldassari/Desktop/zim-cos_ChrX/call_snps_ChrX.py

cd /Users/philipbaldassari/Desktop/zim-cos_ChrX

for file in *.fa
do
	rm $file
done

echo "################################################################################################"
echo "CHROM X SNPs called for each chunk to unfiltered csv files.  Please filter.  Fasta files removed."
echo "################################################################################################"


#Chrom 2L
cd /Users/philipbaldassari/Desktop/zim-cos_Chr2Lseq
python /Users/philipbaldassari/Desktop/zim-cos_Chr2Lseq/fas_chunks_Chr2L.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr2L
bash /Users/philipbaldassari/Desktop/zim-cos_Chr2L/concat_fas_Chr2L.sh

echo "################################################################################################"
echo "fasta alignment chunk files made for Chrom 2L...continuing to call SNPs to csv files."
echo "################################################################################################"

python /Users/philipbaldassari/Desktop/zim-cos_Chr2L/call_snps_Chr2L.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr2L

for file in *.fa
do
	rm $file
done

echo "################################################################################################"
echo "CHROM 2L SNPs called for each chunk to unfiltered csv files.  Please filter.  Fasta files removed."
echo "################################################################################################"


#Chrom 2R
cd /Users/philipbaldassari/Desktop/zim-cos_Chr2Rseq
python /Users/philipbaldassari/Desktop/zim-cos_Chr2Rseq/fas_chunks_Chr2R.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr2R
bash /Users/philipbaldassari/Desktop/zim-cos_Chr2R/concat_fas_Chr2R.sh

echo "################################################################################################"
echo "fasta alignment chunk files made for Chrom 2R...continuing to call SNPs to csv files."
echo "################################################################################################"

python /Users/philipbaldassari/Desktop/zim-cos_Chr2R/call_snps_Chr2R.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr2R

for file in *.fa
do
	rm $file
done

echo "################################################################################################"
echo "CHROM 2R SNPs called for each chunk to unfiltered csv files.  Please filter.  Fasta files removed."
echo "################################################################################################"


#Chrom 3L
cd /Users/philipbaldassari/Desktop/zim-cos_Chr3Lseq
python /Users/philipbaldassari/Desktop/zim-cos_Chr3Lseq/fas_chunks_Chr3L.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr3L
bash /Users/philipbaldassari/Desktop/zim-cos_Chr3L/concat_fas_Chr3L.sh

echo "################################################################################################"
echo "fasta alignment chunk files made for Chrom 3L...continuing to call SNPs to csv files."
echo "################################################################################################"

python /Users/philipbaldassari/Desktop/zim-cos_Chr3L/call_snps_Chr3L.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr3L

for file in *.fa
do
	rm $file
done

echo "################################################################################################"
echo "CHROM 3L SNPs called for each chunk to unfiltered csv files.  Please filter.  Fasta files removed."
echo "################################################################################################"


#Chrom 3R
cd /Users/philipbaldassari/Desktop/zim-cos_Chr3Rseq
python /Users/philipbaldassari/Desktop/zim-cos_Chr3Rseq/fas_chunks_Chr3R.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr3R
bash /Users/philipbaldassari/Desktop/zim-cos_Chr3R/concat_fas_Chr3R.sh

echo "################################################################################################"
echo "fasta alignment chunk files made for Chrom 3R...continuing to call SNPs to csv files."
echo "################################################################################################"

python /Users/philipbaldassari/Desktop/zim-cos_Chr3R/call_snps_Chr3R.py

cd /Users/philipbaldassari/Desktop/zim-cos_Chr3R

for file in *.fa
do
	rm $file
done

echo "################################################################################################"
echo "CHROM 3R SNPs called for each chunk to unfiltered csv files.  Please filter.  Fasta files removed."
echo "################################################################################################"


echo "################################################################################################"
echo "################################################################################################"
echo "All processes complete!  Please filter the data."
echo "################################################################################################"
echo "################################################################################################"




