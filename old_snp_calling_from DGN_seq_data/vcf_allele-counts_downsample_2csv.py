#this script is used to create csv files listing the CHROM, POS, Number of Major Alleles, and  Minor Alleles for each population downsampled to a specific sample size n

#importing modules
import vcf
import numpy as np
import pandas as pd
import random
from multiprocessing import Process

#defining downsampled n for each pop
n_FR = 50
n_RAL = 125
n_SAfr = 40
n_ZI = 180
n_ZH = 3
n_ZW = 6
n_ZS = 4

#ChrX vcf function
def vcf_ChrX_csv():

	print("Starting vcf_ChrX process")
	
	#lists
	chrom = []
	pos = []
	majorFR = []
	majorRAL = []
	majorSAfr = []
	majorZI = []
	majorZH = []
	majorZW = []
	majorZS = []
	minorFR = []
	minorRAL = []
	minorSAfr = []
	minorZI = []
	minorZH = []
	minorZW = []
	minorZS = []
	
	#reading vcf
	vcf_reader = vcf.Reader(open("zim-cos_ChrX.vcf", "r"))
	
	for record in vcf_reader:
		#appending CHROM and POS to lists
		chrom.append(record.CHROM)
		pos.append(record.POS)

		samples = record.samples
		FR = []
		RAL = []
		SAfr = []
		ZI = []
		ZH = []
		ZW = []
		ZS = []

		counter_FR = 0
		counter_RAL = 0
		counter_SAfr = 0
		counter_ZI = 0
		counter_ZH = 0
		counter_ZW = 0
		counter_ZS = 0

		for i in random.sample(samples, len(samples)):
			if "FR" in str(i) and counter_FR < n_FR and ("0/0" in str(i) or "1/1" in str(i)):
				FR.append(i)
				counter_FR += 1
			elif "RAL" in str(i) and counter_RAL < n_RAL and ("0/0" in str(i) or "1/1" in str(i)):
				RAL.append(i)
				counter_RAL += 1
			elif "SD" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "SP" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "ZI" in str(i) and counter_ZI < n_ZI and ("0/0" in str(i) or "1/1" in str(i)):
				ZI.append(i)
				counter_ZI += 1
			elif "ZH" in str(i) and counter_ZH < n_ZH and ("0/0" in str(i) or "1/1" in str(i)):
				ZH.append(i)
				counter_ZH += 1
			elif "ZW" in str(i) and counter_ZW < n_ZW and ("0/0" in str(i) or "1/1" in str(i)):
				ZW.append(i)
				counter_ZW += 1
			elif "ZS" in str(i) and counter_ZS < n_ZS and ("0/0" in str(i) or "1/1" in str(i)):
				ZS.append(i)
				counter_ZS += 1
			else:
				continue

		#counting alleles for each pop
		FR_str = str(FR)
		RAL_str = str(RAL)
		SAfr_str = str(SAfr)
		ZI_str = str(ZI)
		ZH_str = str(ZH)
		ZW_str = str(ZW)
		ZS_str = str(ZS)

		majorFR.append(FR_str.count("0/0"))
		majorRAL.append(RAL_str.count("0/0"))
		majorSAfr.append(SAfr_str.count("0/0"))
		majorZI.append(ZI_str.count("0/0"))
		majorZH.append(ZH_str.count("0/0"))
		majorZW.append(ZW_str.count("0/0"))
		majorZS.append(ZS_str.count("0/0"))

		minorFR.append(FR_str.count("1/1"))
		minorRAL.append(RAL_str.count("1/1"))
		minorSAfr.append(SAfr_str.count("1/1"))
		minorZI.append(ZI_str.count("1/1"))
		minorZH.append(ZH_str.count("1/1"))
		minorZW.append(ZW_str.count("1/1"))
		minorZS.append(ZS_str.count("1/1"))
		
		
	#making dataframe from dictionary
	dictionary = {"CHROM": chrom, "POS": pos, "Major_ac_FR": majorFR, "mac_FR": minorFR, "Major_ac_RAL": majorRAL, "mac_RAL": minorRAL, "Major_ac_SAfr": majorSAfr, "mac_SAfr": minorSAfr, "Major_ac_ZI": majorZI, "mac_ZI": minorZI, "Major_ac_ZH": majorZH, "mac_ZH": minorZH, "Major_ac_ZW": majorZW, "mac_ZW": minorZW, "Major_ac_ZS": majorZS, "mac_ZS": minorZS}

	df = pd.DataFrame(dictionary)

	#editing dataframe
	##n per pop
	df.insert(4, "n_FR", df.Major_ac_FR + df.mac_FR)
	df.insert(7, "n_RAL", df.Major_ac_RAL + df.mac_RAL)
	df.insert(10, "n_SAfr", df.Major_ac_SAfr + df.mac_SAfr)
	df.insert(13, "n_ZI", df.Major_ac_ZI + df.mac_ZI)
	df.insert(16, "n_ZH", df.Major_ac_ZH + df.mac_ZH)
	df.insert(19, "n_ZW", df.Major_ac_ZW + df.mac_ZW)
	df.insert(22, "n_ZS", df.Major_ac_ZS + df.mac_ZS)

	##maf per pop
	df.insert(5, "maf_FR", df.mac_FR / df.n_FR)
	df.insert(8, "maf_RAL", df.mac_RAL / df.n_RAL)
	df.insert(11, "maf_SAfr", df.mac_SAfr / df.n_SAfr)
	df.insert(14, "maf_ZI", df.mac_ZI / df.n_ZI)
	df.insert(17, "maf_ZH", df.mac_ZH / df.n_ZH)
	df.insert(20, "maf_ZW", df.mac_ZW / df.n_ZW)
	df.insert(23, "maf_ZS", df.mac_ZS / df.n_ZS)

	##drop Major_ac columns
	df = df.drop(["Major_ac_FR", "Major_ac_RAL", "Major_ac_SAfr", "Major_ac_ZI", "Major_ac_ZH", "Major_ac_ZW", "Major_ac_ZS"], axis=1)
	
	#dataframe to csv
	df.to_csv('vcf_ChrX_allele-counts_downsample.csv', index=False)

	print("csv for vcf_ChrX saved")


#Chr2L vcf function
def vcf_Chr2L_csv():

	print("Starting vcf_Chr2L process")
	
	#lists
	chrom = []
	pos = []
	majorFR = []
	majorRAL = []
	majorSAfr = []
	majorZI = []
	majorZH = []
	majorZW = []
	majorZS = []
	minorFR = []
	minorRAL = []
	minorSAfr = []
	minorZI = []
	minorZH = []
	minorZW = []
	minorZS = []
	
	#reading vcf
	vcf_reader = vcf.Reader(open("zim-cos_Chr2L.vcf", "r"))
	
	for record in vcf_reader:
		#appending CHROM and POS to lists
		chrom.append(record.CHROM)
		pos.append(record.POS)

		samples = record.samples
		FR = []
		RAL = []
		SAfr = []
		ZI = []
		ZH = []
		ZW = []
		ZS = []

		counter_FR = 0
		counter_RAL = 0
		counter_SAfr = 0
		counter_ZI = 0
		counter_ZH = 0
		counter_ZW = 0
		counter_ZS = 0

		for i in random.sample(samples, len(samples)):
			if "FR" in str(i) and counter_FR < n_FR and ("0/0" in str(i) or "1/1" in str(i)):
				FR.append(i)
				counter_FR += 1
			elif "RAL" in str(i) and counter_RAL < n_RAL and ("0/0" in str(i) or "1/1" in str(i)):
				RAL.append(i)
				counter_RAL += 1
			elif "SD" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "SP" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "ZI" in str(i) and counter_ZI < n_ZI and ("0/0" in str(i) or "1/1" in str(i)):
				ZI.append(i)
				counter_ZI += 1
			elif "ZH" in str(i) and counter_ZH < n_ZH and ("0/0" in str(i) or "1/1" in str(i)):
				ZH.append(i)
				counter_ZH += 1
			elif "ZW" in str(i) and counter_ZW < n_ZW and ("0/0" in str(i) or "1/1" in str(i)):
				ZW.append(i)
				counter_ZW += 1
			elif "ZS" in str(i) and counter_ZS < n_ZS and ("0/0" in str(i) or "1/1" in str(i)):
				ZS.append(i)
				counter_ZS += 1
			else:
				continue

		#counting alleles for each pop
		FR_str = str(FR)
		RAL_str = str(RAL)
		SAfr_str = str(SAfr)
		ZI_str = str(ZI)
		ZH_str = str(ZH)
		ZW_str = str(ZW)
		ZS_str = str(ZS)

		majorFR.append(FR_str.count("0/0"))
		majorRAL.append(RAL_str.count("0/0"))
		majorSAfr.append(SAfr_str.count("0/0"))
		majorZI.append(ZI_str.count("0/0"))
		majorZH.append(ZH_str.count("0/0"))
		majorZW.append(ZW_str.count("0/0"))
		majorZS.append(ZS_str.count("0/0"))

		minorFR.append(FR_str.count("1/1"))
		minorRAL.append(RAL_str.count("1/1"))
		minorSAfr.append(SAfr_str.count("1/1"))
		minorZI.append(ZI_str.count("1/1"))
		minorZH.append(ZH_str.count("1/1"))
		minorZW.append(ZW_str.count("1/1"))
		minorZS.append(ZS_str.count("1/1"))
		
		
	#making dataframe from dictionary
	dictionary = {"CHROM": chrom, "POS": pos, "Major_ac_FR": majorFR, "mac_FR": minorFR, "Major_ac_RAL": majorRAL, "mac_RAL": minorRAL, "Major_ac_SAfr": majorSAfr, "mac_SAfr": minorSAfr, "Major_ac_ZI": majorZI, "mac_ZI": minorZI, "Major_ac_ZH": majorZH, "mac_ZH": minorZH, "Major_ac_ZW": majorZW, "mac_ZW": minorZW, "Major_ac_ZS": majorZS, "mac_ZS": minorZS}

	df = pd.DataFrame(dictionary)

	#editing dataframe
	##n per pop
	df.insert(4, "n_FR", df.Major_ac_FR + df.mac_FR)
	df.insert(7, "n_RAL", df.Major_ac_RAL + df.mac_RAL)
	df.insert(10, "n_SAfr", df.Major_ac_SAfr + df.mac_SAfr)
	df.insert(13, "n_ZI", df.Major_ac_ZI + df.mac_ZI)
	df.insert(16, "n_ZH", df.Major_ac_ZH + df.mac_ZH)
	df.insert(19, "n_ZW", df.Major_ac_ZW + df.mac_ZW)
	df.insert(22, "n_ZS", df.Major_ac_ZS + df.mac_ZS)

	##maf per pop
	df.insert(5, "maf_FR", df.mac_FR / df.n_FR)
	df.insert(8, "maf_RAL", df.mac_RAL / df.n_RAL)
	df.insert(11, "maf_SAfr", df.mac_SAfr / df.n_SAfr)
	df.insert(14, "maf_ZI", df.mac_ZI / df.n_ZI)
	df.insert(17, "maf_ZH", df.mac_ZH / df.n_ZH)
	df.insert(20, "maf_ZW", df.mac_ZW / df.n_ZW)
	df.insert(23, "maf_ZS", df.mac_ZS / df.n_ZS)

	##drop Major_ac columns
	df = df.drop(["Major_ac_FR", "Major_ac_RAL", "Major_ac_SAfr", "Major_ac_ZI", "Major_ac_ZH", "Major_ac_ZW", "Major_ac_ZS"], axis=1)
	
	#dataframe to csv
	df.to_csv('vcf_Chr2L_allele-counts_downsample.csv', index=False)

	print("csv for vcf_Chr2L saved")


#Chr2R vcf function
def vcf_Chr2R_csv():

	print("Starting vcf_Chr2R process")
	
	#lists
	chrom = []
	pos = []
	majorFR = []
	majorRAL = []
	majorSAfr = []
	majorZI = []
	majorZH = []
	majorZW = []
	majorZS = []
	minorFR = []
	minorRAL = []
	minorSAfr = []
	minorZI = []
	minorZH = []
	minorZW = []
	minorZS = []
	
	#reading vcf
	vcf_reader = vcf.Reader(open("zim-cos_Chr2R.vcf", "r"))
	
	for record in vcf_reader:
		#appending CHROM and POS to lists
		chrom.append(record.CHROM)
		pos.append(record.POS)

		samples = record.samples
		FR = []
		RAL = []
		SAfr = []
		ZI = []
		ZH = []
		ZW = []
		ZS = []

		counter_FR = 0
		counter_RAL = 0
		counter_SAfr = 0
		counter_ZI = 0
		counter_ZH = 0
		counter_ZW = 0
		counter_ZS = 0

		for i in random.sample(samples, len(samples)):
			if "FR" in str(i) and counter_FR < n_FR and ("0/0" in str(i) or "1/1" in str(i)):
				FR.append(i)
				counter_FR += 1
			elif "RAL" in str(i) and counter_RAL < n_RAL and ("0/0" in str(i) or "1/1" in str(i)):
				RAL.append(i)
				counter_RAL += 1
			elif "SD" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "SP" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "ZI" in str(i) and counter_ZI < n_ZI and ("0/0" in str(i) or "1/1" in str(i)):
				ZI.append(i)
				counter_ZI += 1
			elif "ZH" in str(i) and counter_ZH < n_ZH and ("0/0" in str(i) or "1/1" in str(i)):
				ZH.append(i)
				counter_ZH += 1
			elif "ZW" in str(i) and counter_ZW < n_ZW and ("0/0" in str(i) or "1/1" in str(i)):
				ZW.append(i)
				counter_ZW += 1
			elif "ZS" in str(i) and counter_ZS < n_ZS and ("0/0" in str(i) or "1/1" in str(i)):
				ZS.append(i)
				counter_ZS += 1
			else:
				continue

		#counting alleles for each pop
		FR_str = str(FR)
		RAL_str = str(RAL)
		SAfr_str = str(SAfr)
		ZI_str = str(ZI)
		ZH_str = str(ZH)
		ZW_str = str(ZW)
		ZS_str = str(ZS)

		majorFR.append(FR_str.count("0/0"))
		majorRAL.append(RAL_str.count("0/0"))
		majorSAfr.append(SAfr_str.count("0/0"))
		majorZI.append(ZI_str.count("0/0"))
		majorZH.append(ZH_str.count("0/0"))
		majorZW.append(ZW_str.count("0/0"))
		majorZS.append(ZS_str.count("0/0"))

		minorFR.append(FR_str.count("1/1"))
		minorRAL.append(RAL_str.count("1/1"))
		minorSAfr.append(SAfr_str.count("1/1"))
		minorZI.append(ZI_str.count("1/1"))
		minorZH.append(ZH_str.count("1/1"))
		minorZW.append(ZW_str.count("1/1"))
		minorZS.append(ZS_str.count("1/1"))
		
		
	#making dataframe from dictionary
	dictionary = {"CHROM": chrom, "POS": pos, "Major_ac_FR": majorFR, "mac_FR": minorFR, "Major_ac_RAL": majorRAL, "mac_RAL": minorRAL, "Major_ac_SAfr": majorSAfr, "mac_SAfr": minorSAfr, "Major_ac_ZI": majorZI, "mac_ZI": minorZI, "Major_ac_ZH": majorZH, "mac_ZH": minorZH, "Major_ac_ZW": majorZW, "mac_ZW": minorZW, "Major_ac_ZS": majorZS, "mac_ZS": minorZS}

	df = pd.DataFrame(dictionary)

	#editing dataframe
	##n per pop
	df.insert(4, "n_FR", df.Major_ac_FR + df.mac_FR)
	df.insert(7, "n_RAL", df.Major_ac_RAL + df.mac_RAL)
	df.insert(10, "n_SAfr", df.Major_ac_SAfr + df.mac_SAfr)
	df.insert(13, "n_ZI", df.Major_ac_ZI + df.mac_ZI)
	df.insert(16, "n_ZH", df.Major_ac_ZH + df.mac_ZH)
	df.insert(19, "n_ZW", df.Major_ac_ZW + df.mac_ZW)
	df.insert(22, "n_ZS", df.Major_ac_ZS + df.mac_ZS)

	##maf per pop
	df.insert(5, "maf_FR", df.mac_FR / df.n_FR)
	df.insert(8, "maf_RAL", df.mac_RAL / df.n_RAL)
	df.insert(11, "maf_SAfr", df.mac_SAfr / df.n_SAfr)
	df.insert(14, "maf_ZI", df.mac_ZI / df.n_ZI)
	df.insert(17, "maf_ZH", df.mac_ZH / df.n_ZH)
	df.insert(20, "maf_ZW", df.mac_ZW / df.n_ZW)
	df.insert(23, "maf_ZS", df.mac_ZS / df.n_ZS)

	##drop Major_ac columns
	df = df.drop(["Major_ac_FR", "Major_ac_RAL", "Major_ac_SAfr", "Major_ac_ZI", "Major_ac_ZH", "Major_ac_ZW", "Major_ac_ZS"], axis=1)
	
	#dataframe to csv
	df.to_csv('vcf_Chr2R_allele-counts_downsample.csv', index=False)

	print("csv for vcf_Chr2R saved")


#Chr3L vcf function
def vcf_Chr3L_csv():

	print("Starting vcf_Chr3L process")
	
	#lists
	chrom = []
	pos = []
	majorFR = []
	majorRAL = []
	majorSAfr = []
	majorZI = []
	majorZH = []
	majorZW = []
	majorZS = []
	minorFR = []
	minorRAL = []
	minorSAfr = []
	minorZI = []
	minorZH = []
	minorZW = []
	minorZS = []
	
	#reading vcf
	vcf_reader = vcf.Reader(open("zim-cos_Chr3L.vcf", "r"))
	
	for record in vcf_reader:
		#appending CHROM and POS to lists
		chrom.append(record.CHROM)
		pos.append(record.POS)

		samples = record.samples
		FR = []
		RAL = []
		SAfr = []
		ZI = []
		ZH = []
		ZW = []
		ZS = []

		counter_FR = 0
		counter_RAL = 0
		counter_SAfr = 0
		counter_ZI = 0
		counter_ZH = 0
		counter_ZW = 0
		counter_ZS = 0

		for i in random.sample(samples, len(samples)):
			if "FR" in str(i) and counter_FR < n_FR and ("0/0" in str(i) or "1/1" in str(i)):
				FR.append(i)
				counter_FR += 1
			elif "RAL" in str(i) and counter_RAL < n_RAL and ("0/0" in str(i) or "1/1" in str(i)):
				RAL.append(i)
				counter_RAL += 1
			elif "SD" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "SP" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "ZI" in str(i) and counter_ZI < n_ZI and ("0/0" in str(i) or "1/1" in str(i)):
				ZI.append(i)
				counter_ZI += 1
			elif "ZH" in str(i) and counter_ZH < n_ZH and ("0/0" in str(i) or "1/1" in str(i)):
				ZH.append(i)
				counter_ZH += 1
			elif "ZW" in str(i) and counter_ZW < n_ZW and ("0/0" in str(i) or "1/1" in str(i)):
				ZW.append(i)
				counter_ZW += 1
			elif "ZS" in str(i) and counter_ZS < n_ZS and ("0/0" in str(i) or "1/1" in str(i)):
				ZS.append(i)
				counter_ZS += 1
			else:
				continue

		#counting alleles for each pop
		FR_str = str(FR)
		RAL_str = str(RAL)
		SAfr_str = str(SAfr)
		ZI_str = str(ZI)
		ZH_str = str(ZH)
		ZW_str = str(ZW)
		ZS_str = str(ZS)

		majorFR.append(FR_str.count("0/0"))
		majorRAL.append(RAL_str.count("0/0"))
		majorSAfr.append(SAfr_str.count("0/0"))
		majorZI.append(ZI_str.count("0/0"))
		majorZH.append(ZH_str.count("0/0"))
		majorZW.append(ZW_str.count("0/0"))
		majorZS.append(ZS_str.count("0/0"))

		minorFR.append(FR_str.count("1/1"))
		minorRAL.append(RAL_str.count("1/1"))
		minorSAfr.append(SAfr_str.count("1/1"))
		minorZI.append(ZI_str.count("1/1"))
		minorZH.append(ZH_str.count("1/1"))
		minorZW.append(ZW_str.count("1/1"))
		minorZS.append(ZS_str.count("1/1"))
		
		
	#making dataframe from dictionary
	dictionary = {"CHROM": chrom, "POS": pos, "Major_ac_FR": majorFR, "mac_FR": minorFR, "Major_ac_RAL": majorRAL, "mac_RAL": minorRAL, "Major_ac_SAfr": majorSAfr, "mac_SAfr": minorSAfr, "Major_ac_ZI": majorZI, "mac_ZI": minorZI, "Major_ac_ZH": majorZH, "mac_ZH": minorZH, "Major_ac_ZW": majorZW, "mac_ZW": minorZW, "Major_ac_ZS": majorZS, "mac_ZS": minorZS}

	df = pd.DataFrame(dictionary)

	#editing dataframe
	##n per pop
	df.insert(4, "n_FR", df.Major_ac_FR + df.mac_FR)
	df.insert(7, "n_RAL", df.Major_ac_RAL + df.mac_RAL)
	df.insert(10, "n_SAfr", df.Major_ac_SAfr + df.mac_SAfr)
	df.insert(13, "n_ZI", df.Major_ac_ZI + df.mac_ZI)
	df.insert(16, "n_ZH", df.Major_ac_ZH + df.mac_ZH)
	df.insert(19, "n_ZW", df.Major_ac_ZW + df.mac_ZW)
	df.insert(22, "n_ZS", df.Major_ac_ZS + df.mac_ZS)

	##maf per pop
	df.insert(5, "maf_FR", df.mac_FR / df.n_FR)
	df.insert(8, "maf_RAL", df.mac_RAL / df.n_RAL)
	df.insert(11, "maf_SAfr", df.mac_SAfr / df.n_SAfr)
	df.insert(14, "maf_ZI", df.mac_ZI / df.n_ZI)
	df.insert(17, "maf_ZH", df.mac_ZH / df.n_ZH)
	df.insert(20, "maf_ZW", df.mac_ZW / df.n_ZW)
	df.insert(23, "maf_ZS", df.mac_ZS / df.n_ZS)

	##drop Major_ac columns
	df = df.drop(["Major_ac_FR", "Major_ac_RAL", "Major_ac_SAfr", "Major_ac_ZI", "Major_ac_ZH", "Major_ac_ZW", "Major_ac_ZS"], axis=1)
	
	#dataframe to csv
	df.to_csv('vcf_Chr3L_allele-counts_downsample.csv', index=False)

	print("csv for vcf_Chr3L saved")


#Chr3R vcf function
def vcf_Chr3R_csv():

	print("Starting vcf_Chr3R process")
	
	#lists
	chrom = []
	pos = []
	majorFR = []
	majorRAL = []
	majorSAfr = []
	majorZI = []
	majorZH = []
	majorZW = []
	majorZS = []
	minorFR = []
	minorRAL = []
	minorSAfr = []
	minorZI = []
	minorZH = []
	minorZW = []
	minorZS = []
	
	#reading vcf
	vcf_reader = vcf.Reader(open("zim-cos_Chr3R.vcf", "r"))
	
	for record in vcf_reader:
		#appending CHROM and POS to lists
		chrom.append(record.CHROM)
		pos.append(record.POS)

		samples = record.samples
		FR = []
		RAL = []
		SAfr = []
		ZI = []
		ZH = []
		ZW = []
		ZS = []

		counter_FR = 0
		counter_RAL = 0
		counter_SAfr = 0
		counter_ZI = 0
		counter_ZH = 0
		counter_ZW = 0
		counter_ZS = 0

		for i in random.sample(samples, len(samples)):
			if "FR" in str(i) and counter_FR < n_FR and ("0/0" in str(i) or "1/1" in str(i)):
				FR.append(i)
				counter_FR += 1
			elif "RAL" in str(i) and counter_RAL < n_RAL and ("0/0" in str(i) or "1/1" in str(i)):
				RAL.append(i)
				counter_RAL += 1
			elif "SD" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "SP" in str(i) and counter_SAfr < n_SAfr and ("0/0" in str(i) or "1/1" in str(i)):
				SAfr.append(i)
				counter_SAfr += 1
			elif "ZI" in str(i) and counter_ZI < n_ZI and ("0/0" in str(i) or "1/1" in str(i)):
				ZI.append(i)
				counter_ZI += 1
			elif "ZH" in str(i) and counter_ZH < n_ZH and ("0/0" in str(i) or "1/1" in str(i)):
				ZH.append(i)
				counter_ZH += 1
			elif "ZW" in str(i) and counter_ZW < n_ZW and ("0/0" in str(i) or "1/1" in str(i)):
				ZW.append(i)
				counter_ZW += 1
			elif "ZS" in str(i) and counter_ZS < n_ZS and ("0/0" in str(i) or "1/1" in str(i)):
				ZS.append(i)
				counter_ZS += 1
			else:
				continue

		#counting alleles for each pop
		FR_str = str(FR)
		RAL_str = str(RAL)
		SAfr_str = str(SAfr)
		ZI_str = str(ZI)
		ZH_str = str(ZH)
		ZW_str = str(ZW)
		ZS_str = str(ZS)

		majorFR.append(FR_str.count("0/0"))
		majorRAL.append(RAL_str.count("0/0"))
		majorSAfr.append(SAfr_str.count("0/0"))
		majorZI.append(ZI_str.count("0/0"))
		majorZH.append(ZH_str.count("0/0"))
		majorZW.append(ZW_str.count("0/0"))
		majorZS.append(ZS_str.count("0/0"))

		minorFR.append(FR_str.count("1/1"))
		minorRAL.append(RAL_str.count("1/1"))
		minorSAfr.append(SAfr_str.count("1/1"))
		minorZI.append(ZI_str.count("1/1"))
		minorZH.append(ZH_str.count("1/1"))
		minorZW.append(ZW_str.count("1/1"))
		minorZS.append(ZS_str.count("1/1"))
		
		
	#making dataframe from dictionary
	dictionary = {"CHROM": chrom, "POS": pos, "Major_ac_FR": majorFR, "mac_FR": minorFR, "Major_ac_RAL": majorRAL, "mac_RAL": minorRAL, "Major_ac_SAfr": majorSAfr, "mac_SAfr": minorSAfr, "Major_ac_ZI": majorZI, "mac_ZI": minorZI, "Major_ac_ZH": majorZH, "mac_ZH": minorZH, "Major_ac_ZW": majorZW, "mac_ZW": minorZW, "Major_ac_ZS": majorZS, "mac_ZS": minorZS}

	df = pd.DataFrame(dictionary)

	#editing dataframe
	##n per pop
	df.insert(4, "n_FR", df.Major_ac_FR + df.mac_FR)
	df.insert(7, "n_RAL", df.Major_ac_RAL + df.mac_RAL)
	df.insert(10, "n_SAfr", df.Major_ac_SAfr + df.mac_SAfr)
	df.insert(13, "n_ZI", df.Major_ac_ZI + df.mac_ZI)
	df.insert(16, "n_ZH", df.Major_ac_ZH + df.mac_ZH)
	df.insert(19, "n_ZW", df.Major_ac_ZW + df.mac_ZW)
	df.insert(22, "n_ZS", df.Major_ac_ZS + df.mac_ZS)

	##maf per pop
	df.insert(5, "maf_FR", df.mac_FR / df.n_FR)
	df.insert(8, "maf_RAL", df.mac_RAL / df.n_RAL)
	df.insert(11, "maf_SAfr", df.mac_SAfr / df.n_SAfr)
	df.insert(14, "maf_ZI", df.mac_ZI / df.n_ZI)
	df.insert(17, "maf_ZH", df.mac_ZH / df.n_ZH)
	df.insert(20, "maf_ZW", df.mac_ZW / df.n_ZW)
	df.insert(23, "maf_ZS", df.mac_ZS / df.n_ZS)

	##drop Major_ac columns
	df = df.drop(["Major_ac_FR", "Major_ac_RAL", "Major_ac_SAfr", "Major_ac_ZI", "Major_ac_ZH", "Major_ac_ZW", "Major_ac_ZS"], axis=1)
	
	#dataframe to csv
	df.to_csv('vcf_Chr3R_allele-counts_downsample.csv', index=False)

	print("csv for vcf_Chr3R saved")


#Running concurrently
if __name__ == '__main__':
	pX = Process(target=vcf_ChrX_csv)
	pX.start()
	
	p2L = Process(target=vcf_Chr2L_csv)
	p2L.start()
	
	p2R = Process(target=vcf_Chr2R_csv)
	p2R.start()
	
	p3L = Process(target=vcf_Chr3L_csv)
	p3L.start()
	
	p3R = Process(target=vcf_Chr3R_csv)
	p3R.start()
	
	pX.join()
	p2L.join()
	p2R.join()
	p3L.join()
	p3R.join()






