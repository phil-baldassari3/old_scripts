#!/bin/bash

echo "Converting flybase r5 coordinates to r6 coordinates from csv files."

cd /Users/philipbaldassari/Desktop/zim_cos_fst_data


echo "scraping r5 coordinates from csvs"

python coordinate_scraper_r5.py

echo "done scraping r5 coordinates from csvs"
echo "starting conversion process"

for file in r5*.txt
do
	/Users/philipbaldassari/Desktop/dmel_r5_to_r6/dmel_r5_to_r6_converter.pl --input $file --output r6_$file
done

echo "bookkeeping..."

for file in r5*.txt
do
	rm $file
done

echo "The coordinate_scraper_r6.py python script needs to be prepared for multiprocessing"
echo "Here are the files that this script will be run on:"
echo ""

ls r6_r5*.txt

echo ""


echo "scraping r6 coordinates from r5 to r6 conversion files"

python coordinate_scraper_r6.py

echo "done scraping r6 coordinates from conversion files"
echo "bookkeeping..."

for file in *temp.csv
do
	rm $file
done

for file in r6_r5*.txt
do
	rm $file
done


echo ""
echo "All processes complete. All flybase r5 coordinates have been converted to r6"
echo ""
echo ""
echo "MAKE SURE TO REMOVE SITES ON WHICH THE CONVERSION HAS FAILED (check .failed files)"









