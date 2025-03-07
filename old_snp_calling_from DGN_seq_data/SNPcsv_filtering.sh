#!/bin/bash

echo "Filtering Singletons and Triallelic SNPs from csv SNP data"

#Chrom X
cd /Users/philipbaldassari/Desktop/zim-cos_ChrX
python /Users/philipbaldassari/Desktop/zim-cos_ChrX/filter_SNP_csvs_ChrX.py

echo "################################################################################################"
echo "################################################################################################"

#Chrom 2L
cd /Users/philipbaldassari/Desktop/zim-cos_Chr2L
python /Users/philipbaldassari/Desktop/zim-cos_Chr2L/filter_SNP_csvs_Chr2L.py

echo "################################################################################################"
echo "################################################################################################"

#Chrom 2R
cd /Users/philipbaldassari/Desktop/zim-cos_Chr2R
python /Users/philipbaldassari/Desktop/zim-cos_Chr2R/filter_SNP_csvs_Chr2R.py

echo "################################################################################################"
echo "################################################################################################"

#Chrom 3L
cd /Users/philipbaldassari/Desktop/zim-cos_Chr3L
python /Users/philipbaldassari/Desktop/zim-cos_Chr3L/filter_SNP_csvs_Chr3L.py

echo "################################################################################################"
echo "################################################################################################"

#Chrom 3R
cd /Users/philipbaldassari/Desktop/zim-cos_Chr3R
python /Users/philipbaldassari/Desktop/zim-cos_Chr3R/filter_SNP_csvs_Chr3R.py


echo "################################################################################################"
echo "DONE FILTRATION. FILES OVERWRITTEN."
echo "################################################################################################"
