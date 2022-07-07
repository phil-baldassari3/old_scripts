#script to downsample SNP data from the SNP csv files. will return dataframes with allele frequencies and population counts. data must be filtered first.

#importing modules
import os,sys
import pandas as pd
import numpy as np
from multiprocessing import Pool
import random

#setting directory
directory = "set"

'''
#get list of csvs for parallel pool mapping
file_list = []

for file in os.listdir(directory):
    if file.endswith('.csv'):
        file_list.append(file)
    else:
        continue

print(file_list)
'''

#defining downsampled n for each pop
FR_n = 40
RAL_n = 100
SAfr_n = 40
ZI_n = 100
ZH_n = 3
ZW_n = 6
ZS_n = 4

#downsampling function
def snp_csv_downsample(infile):

    print('starting process for ' + infile)

    #set Chrom
    chrom = 'Chr'
    
    #lists
    n_FR = []
    n_RAL = []
    n_SAfr = []
    n_ZI = []
    n_ZH = []
    n_ZW = []
    n_ZS = []
    maf_FR = []
    maf_RAL = []
    maf_SAfr = []
    maf_ZI = []
    maf_ZH = []
    maf_ZW = []
    maf_ZS = []

    #open dataframe
    loci = pd.read_csv(infile)
    #locus dataframe
    loci.drop(loci.columns.difference(['Locus']), axis=1, inplace=True)

    #open dataframe
    df = pd.read_csv(infile)

    print('looping through rows and downsampling by population for ' + infile)

    #finding the major allele
    conditions  = [(df['Acount'] >= df['Tcount']) & (df['Acount'] >= df['Ccount']) & (df['Acount'] >= df['Gcount']), (df['Tcount'] >= df['Acount']) & (df['Tcount'] >= df['Ccount']) & (df['Tcount'] >= df['Gcount']), (df['Ccount'] >= df['Acount']) & (df['Ccount'] >= df['Tcount']) & (df['Ccount'] >= df['Gcount']), (df['Gcount'] >= df['Acount']) & (df['Gcount'] >= df['Tcount']) & (df['Gcount'] >= df['Ccount'])]
    choices     = ['adenine', 'thymine', 'cytosine', 'guanine']
    
    df["Major_allele"] = np.select(conditions, choices, default=np.nan)

    ###for each population

    ##FR
    FR_df = df.filter(["FR106N", "FR109N", "FR110N", "FR112N", "FR113N", "FR115N", "FR11N", "FR126N", "FR12N", "FR135N", "FR147N", "FR152N", "FR153N", "FR157N", "FR158N", "FR161N", "FR162N", "FR164N", "FR169N", "FR16N", "FR173N", "FR186N", "FR188N", "FR198N", "FR19N", "FR200N", "FR208N", "FR213N", "FR216N", "FR219N", "FR21N", "FR222N", "FR225N", "FR230N", "FR231N", "FR232N", "FR235N", "FR236N", "FR238N", "FR240N", "FR248N", "FR252N", "FR257N", "FR260N", "FR261N", "FR263N", "FR264N", "FR269N", "FR26N", "FR276N", "FR279N", "FR284N", "FR288N", "FR28N", "FR293N", "FR296N", "FR299N", "FR2N", "FR302N", "FR304N", "FR305N", "FR312N", "FR313N", "FR319N", "FR320N", "FR323N", "FR326N", "FR32N", "FR340N", "FR345N", "FR348N", "FR34N", "FR357N", "FR360N", "FR364N", "FR370N", "FR37N", "FR48N", "FR54N", "FR59N", "FR5N", "FR60N", "FR73N", "FR89N", "FR90N", "FR91N", "FR94N", "Major_allele"], axis=1)

    for row in FR_df.itertuples():

        FR_row_list = list(row)

        #finding major allele
        if 'adenine' in FR_row_list:
            major_allele = "A"
        elif 'thymine' in FR_row_list:
            major_allele = "T"
        elif 'cytosine' in FR_row_list:
            major_allele = "C"
        elif 'guanine' in FR_row_list:
            major_allele = "G"

        #list downsampling
        no_N_FR_row = [value for value in FR_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]  # new_list = [value for value in list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_FR_row = random.sample(no_N_FR_row, len(no_N_FR_row))
        downsample_FR = random_FR_row[0:FR_n]

        #sample size
        bpcount_FR = len(downsample_FR)

        #maf
        if bpcount_FR == 0:
            freq_FR = np.nan
        else:
            freq_FR = 1 - (downsample_FR.count(major_allele) / bpcount_FR)

        #appending
        n_FR.append(bpcount_FR)
        maf_FR.append(freq_FR)

    ##RAL
    RAL_df = df.filter(["RAL-100", "RAL-101", "RAL-105", "RAL-109", "RAL-129", "RAL-136", "RAL-138", "RAL-142", "RAL-149", "RAL-153", "RAL-158", "RAL-161", "RAL-176", "RAL-177", "RAL-181", "RAL-189", "RAL-195", "RAL-208", "RAL-217", "RAL-21", "RAL-223", "RAL-227", "RAL-228", "RAL-229", "RAL-233", "RAL-235", "RAL-237", "RAL-239", "RAL-256", "RAL-26", "RAL-280", "RAL-287", "RAL-28", "RAL-301", "RAL-303", "RAL-304", "RAL-306", "RAL-307", "RAL-309", "RAL-310", "RAL-313", "RAL-315", "RAL-317", "RAL-318", "RAL-319", "RAL-31", "RAL-320", "RAL-321", "RAL-324", "RAL-325", "RAL-32", "RAL-332", "RAL-335", "RAL-336", "RAL-338", "RAL-340", "RAL-348", "RAL-350", "RAL-352", "RAL-354", "RAL-355", "RAL-356", "RAL-357", "RAL-358", "RAL-359", "RAL-360", "RAL-361", "RAL-362", "RAL-365", "RAL-367", "RAL-370", "RAL-371", "RAL-373", "RAL-374", "RAL-375", "RAL-377", "RAL-379", "RAL-380", "RAL-381", "RAL-382", "RAL-383", "RAL-385", "RAL-386", "RAL-38", "RAL-390", "RAL-391", "RAL-392", "RAL-395", "RAL-397", "RAL-399", "RAL-405", "RAL-406", "RAL-409", "RAL-40", "RAL-41", "RAL-426", "RAL-427", "RAL-42", "RAL-437", "RAL-439", "RAL-440", "RAL-441", "RAL-443", "RAL-45", "RAL-461", "RAL-486", "RAL-48", "RAL-491", "RAL-492", "RAL-49", "RAL-502", "RAL-505", "RAL-508", "RAL-509", "RAL-513", "RAL-517", "RAL-528", "RAL-530", "RAL-531", "RAL-535", "RAL-551", "RAL-555", "RAL-559", "RAL-563", "RAL-566", "RAL-57", "RAL-584", "RAL-589", "RAL-595", "RAL-596", "RAL-59", "RAL-627", "RAL-630", "RAL-634", "RAL-639", "RAL-642", "RAL-646", "RAL-69", "RAL-703", "RAL-705", "RAL-707", "RAL-712", "RAL-714", "RAL-716", "RAL-721", "RAL-727", "RAL-730", "RAL-732", "RAL-737", "RAL-738", "RAL-73", "RAL-748", "RAL-757", "RAL-75", "RAL-761", "RAL-765", "RAL-774", "RAL-776", "RAL-783", "RAL-786", "RAL-787", "RAL-790", "RAL-796", "RAL-799", "RAL-801", "RAL-802", "RAL-804", "RAL-805", "RAL-808", "RAL-810", "RAL-812", "RAL-818", "RAL-819", "RAL-820", "RAL-821", "RAL-822", "RAL-832", "RAL-837", "RAL-83", "RAL-843", "RAL-849", "RAL-850", "RAL-852", "RAL-853", "RAL-855", "RAL-857", "RAL-859", "RAL-85", "RAL-861", "RAL-879", "RAL-882", "RAL-884", "RAL-887", "RAL-88", "RAL-890", "RAL-892", "RAL-894", "RAL-897", "RAL-900", "RAL-907", "RAL-908", "RAL-911", "RAL-913", "RAL-91", "RAL-93" ,"Major_allele"], axis=1)

    for row in RAL_df.itertuples():

        RAL_row_list = list(row)

        #finding major allele
        if 'adenine' in RAL_row_list:
            major_allele = "A"
        elif 'thymine' in RAL_row_list:
            major_allele = "T"
        elif 'cytosine' in RAL_row_list:
            major_allele = "C"
        elif 'guanine' in RAL_row_list:
            major_allele = "G"
        
        #list downsampling
        no_N_RAL_row = [value for value in RAL_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_RAL_row = random.sample(no_N_RAL_row, len(no_N_RAL_row))
        downsample_RAL = random_RAL_row[0:RAL_n]

        #sample size
        bpcount_RAL = len(downsample_RAL)

        #maf
        if bpcount_RAL == 0:
            freq_RAL = np.nan
        else:
            freq_RAL = 1 - (downsample_RAL.count(major_allele) / bpcount_RAL)

        #appending
        n_RAL.append(bpcount_RAL)
        maf_RAL.append(freq_RAL)

    ##SAfr
    SAfr_df = df.filter(["SD101N", "SD104N", "SD105N", "SD106N", "SD108N", "SD109N", "SD110N", "SD113N", "SD114N", "SD115N", "SD116N", "SD117N", "SD120N", "SD121N", "SD124N", "SD127N", "SD128N", "SD130N", "SD131N", "SD132N", "SD133N", "SD135N", "SD137N", "SD138N", "SD140N", "SD141N", "SD142N", "SD144N", "SD149N", "SD14N", "SD151N", "SD17N", "SD18N", "SD1N", "SD20N", "SD21N", "SD23N", "SD24N", "SD25N", "SD27N", "SD28N", "SD29N", "SD32N", "SD35N", "SD37N", "SD38N", "SD39N", "SD3N", "SD42N", "SD43N", "SD44N", "SD47N", "SD48N", "SD49N", "SD51N", "SD53N", "SD54N", "SD55N", "SD56N", "SD59N", "SD5N", "SD63N", "SD64N", "SD65N", "SD68N", "SD71N", "SD72N", "SD73N", "SD77N", "SD78N", "SD79N", "SD88N", "SD8N", "SD90N", "SD92N", "SD94N", "SP103N", "SP107N", "SP115N", "SP127N", "SP133N", "SP159N", "SP15N", "SP173", "SP175N", "SP17N", "SP188", "SP191N", "SP19N", "SP1N", "SP201N", "SP213N", "SP221", "SP235", "SP241", "SP249N", "SP254", "SP267N", "SP279N", "SP287N", "SP291N", "SP315N", "SP323N", "SP335N", "SP347N", "SP39N", "SP61N", "SP69N", "SP75N", "SP80", "SP83N", "SP87N", "SP95N" ,"Major_allele"], axis=1)

    for row in SAfr_df.itertuples():

        SAfr_row_list = list(row)

        #finding major allele
        if 'adenine' in SAfr_row_list:
            major_allele = "A"
        elif 'thymine' in SAfr_row_list:
            major_allele = "T"
        elif 'cytosine' in SAfr_row_list:
            major_allele = "C"
        elif 'guanine' in SAfr_row_list:
            major_allele = "G"
        
        #list downsampling
        no_N_SAfr_row = [value for value in SAfr_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_SAfr_row = random.sample(no_N_SAfr_row, len(no_N_SAfr_row))
        downsample_SAfr = random_SAfr_row[0:SAfr_n]

        #sample size
        bpcount_SAfr = len(downsample_SAfr)

        #maf
        if bpcount_SAfr == 0:
            freq_SAfr = np.nan
        else:
            freq_SAfr = 1 - (downsample_SAfr.count(major_allele) / bpcount_SAfr)

        #appending
        n_SAfr.append(bpcount_SAfr)
        maf_SAfr.append(freq_SAfr)

    ##ZI
    ZI_df = df.filter(["ZI103", "ZI104", "ZI10", "ZI114N", "ZI117", "ZI118N", "ZI126", "ZI129", "ZI134N", "ZI136", "ZI138", "ZI152", "ZI157", "ZI161", "ZI164", "ZI165", "ZI167", "ZI170", "ZI172", "ZI173", "ZI176", "ZI177", "ZI178", "ZI179", "ZI181", "ZI182", "ZI184", "ZI185", "ZI188", "ZI190", "ZI191", "ZI193", "ZI194", "ZI196", "ZI197N", "ZI198", "ZI199", "ZI200", "ZI202", "ZI206", "ZI207", "ZI210", "ZI211", "ZI212", "ZI213", "ZI214", "ZI216N", "ZI218", "ZI219", "ZI220", "ZI221", "ZI225", "ZI226", "ZI227", "ZI228", "ZI230", "ZI231", "ZI232", "ZI233", "ZI235", "ZI237", "ZI239", "ZI240", "ZI241", "ZI250", "ZI251N", "ZI252", "ZI253", "ZI254N", "ZI255", "ZI261", "ZI263", "ZI264", "ZI265", "ZI267", "ZI268", "ZI269", "ZI26", "ZI271", "ZI273N", "ZI276", "ZI279", "ZI27", "ZI281", "ZI284", "ZI286", "ZI28", "ZI291", "ZI292", "ZI293", "ZI295", "ZI296", "ZI303", "ZI311N", "ZI313", "ZI314", "ZI316", "ZI317", "ZI319", "ZI31N", "ZI320", "ZI321", "ZI324", "ZI329", "ZI332", "ZI333", "ZI335", "ZI336", "ZI339", "ZI33", "ZI341", "ZI342", "ZI344", "ZI348", "ZI351", "ZI352", "ZI353", "ZI357N", "ZI358", "ZI359", "ZI362", "ZI364", "ZI365", "ZI368", "ZI370", "ZI373", "ZI374", "ZI377", "ZI378", "ZI379", "ZI380", "ZI381", "ZI384", "ZI386", "ZI388", "ZI392", "ZI394N", "ZI395", "ZI396", "ZI397N", "ZI398", "ZI400", "ZI402", "ZI405", "ZI413", "ZI418N", "ZI420", "ZI421", "ZI429", "ZI431", "ZI433", "ZI437", "ZI443", "ZI444", "ZI445", "ZI446", "ZI447", "ZI448", "ZI453", "ZI455N", "ZI456", "ZI457", "ZI458", "ZI460", "ZI466", "ZI467", "ZI468", "ZI471", "ZI472", "ZI476", "ZI477", "ZI486", "ZI488", "ZI490", "ZI491", "ZI504", "ZI505", "ZI508", "ZI50N", "ZI514N", "ZI517", "ZI523", "ZI524", "ZI527", "ZI530", "ZI56", "ZI59", "ZI61", "ZI68", "ZI76", "ZI81", "ZI85", "ZI86", "ZI90", "ZI91", "ZI99" ,"Major_allele"], axis=1)

    for row in ZI_df.itertuples():

        ZI_row_list = list(row)

        #finding major allele
        if 'adenine' in ZI_row_list:
            major_allele = "A"
        elif 'thymine' in ZI_row_list:
            major_allele = "T"
        elif 'cytosine' in ZI_row_list:
            major_allele = "C"
        elif 'guanine' in ZI_row_list:
            major_allele = "G"

        #list downsampling
        no_N_ZI_row = [value for value in ZI_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_ZI_row = random.sample(no_N_ZI_row, len(no_N_ZI_row))
        downsample_ZI = random_ZI_row[0:ZI_n]

        #sample size
        bpcount_ZI = len(downsample_ZI)

        #maf
        if bpcount_ZI == 0:
            freq_ZI = np.nan
        else:
            freq_ZI = 1 - (downsample_ZI.count(major_allele) / bpcount_ZI)

        #appending
        n_ZI.append(bpcount_ZI)
        maf_ZI.append(freq_ZI)

    ##ZH
    ZH_df = df.filter(["ZH23", "ZH26", "ZH33", "ZH42" ,"Major_allele"], axis=1)

    for row in ZH_df.itertuples():

        ZH_row_list = list(row)

        #finding major allele
        if 'adenine' in ZH_row_list:
            major_allele = "A"
        elif 'thymine' in ZH_row_list:
            major_allele = "T"
        elif 'cytosine' in ZH_row_list:
            major_allele = "C"
        elif 'guanine' in ZH_row_list:
            major_allele = "G"

        #list downsampling
        no_N_ZH_row = [value for value in ZH_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_ZH_row = random.sample(no_N_ZH_row, len(no_N_ZH_row))
        downsample_ZH = random_ZH_row[0:ZH_n]

        #sample size
        bpcount_ZH = len(downsample_ZH)

        #maf
        if bpcount_ZH == 0:
            freq_ZH = np.nan
        else:
            freq_ZH = 1 - (downsample_ZH.count(major_allele) / bpcount_ZH)

        #appending
        n_ZH.append(bpcount_ZH)
        maf_ZH.append(freq_ZH)

    ##ZW
    ZW_df = df.filter(["ZW09", "ZW139", "ZW140", "ZW142", "ZW144", "ZW155", "ZW177", "ZW184", "ZW185" ,"Major_allele"], axis=1)

    for row in ZW_df.itertuples():

        ZW_row_list = list(row)

        #finding major allele
        if 'adenine' in ZW_row_list:
            major_allele = "A"
        elif 'thymine' in ZW_row_list:
            major_allele = "T"
        elif 'cytosine' in ZW_row_list:
            major_allele = "C"
        elif 'guanine' in ZW_row_list:
            major_allele = "G"

        #list downsampling
        no_N_ZW_row = [value for value in ZW_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_ZW_row = random.sample(no_N_ZW_row, len(no_N_ZW_row))
        downsample_ZW = random_ZW_row[0:ZW_n]

        #sample size
        bpcount_ZW = len(downsample_ZW)

        #maf
        if bpcount_ZW == 0:
            freq_ZW = np.nan
        else:
            freq_ZW = 1 - (downsample_ZW.count(major_allele) / bpcount_ZW)

        #appending
        n_ZW.append(bpcount_ZW)
        maf_ZW.append(freq_ZW)

    ##ZS
    ZS_df = df.filter(["ZS10", "ZS11", "ZS37", "ZS56", "ZS5" ,"Major_allele"], axis=1)

    for row in ZS_df.itertuples():

        ZS_row_list = list(row)

        #finding major allele
        if 'adenine' in ZS_row_list:
            major_allele = "A"
        elif 'thymine' in ZS_row_list:
            major_allele = "T"
        elif 'cytosine' in ZS_row_list:
            major_allele = "C"
        elif 'guanine' in ZS_row_list:
            major_allele = "G"

        #list downsampling
        no_N_ZS_row = [value for value in ZS_row_list if (value == 'A') | (value == 'T') | (value =='C') | (value =='G')]
        random_ZS_row = random.sample(no_N_ZS_row, len(no_N_ZS_row))
        downsample_ZS = random_ZS_row[0:ZS_n]

        #sample size
        bpcount_ZS = len(downsample_ZS)

        #maf
        if bpcount_ZS == 0:
            freq_ZS = np.nan
        else:
            freq_ZS = 1 - (downsample_ZS.count(major_allele) / bpcount_ZS)

        #appending
        n_ZS.append(bpcount_ZS)
        maf_ZS.append(freq_ZS)

    #dictionary to dataframe
    dictionary = {'n_FR': n_FR, 'maf_FR': maf_FR, 'n_RAL': n_RAL, 'maf_RAL': maf_RAL, 'n_SAfr': n_SAfr, 'maf_SAfr': maf_SAfr, 'n_ZI': n_ZI, 'maf_ZI': maf_ZI, 'n_ZH': n_ZH, 'maf_ZH': maf_ZH, 'n_ZW': n_ZW, 'maf_ZW': maf_ZW, 'n_ZS': n_ZS, 'maf_ZS': maf_ZS}

    data_df = pd.DataFrame(dictionary)

    #merge dataframes
    n_freq_df = pd.merge(loci, data_df, left_index=True, right_index=True)

    #adding chrom column
    n_freq_df.insert(0, 'Chrom', chrom)

    #zim composite populations
    n_freq_df['n_ZH_ZW'] = n_freq_df['n_ZH'] + n_freq_df['n_ZW']
    n_freq_df['maf_ZH_ZW'] = ((n_freq_df['maf_ZH'] * n_freq_df['n_ZH']) + (n_freq_df['maf_ZW'] * n_freq_df['n_ZW'])) / n_freq_df['n_ZH_ZW']
    n_freq_df['n_zim'] = n_freq_df['n_ZH'] + n_freq_df['n_ZW'] + n_freq_df['n_ZS']
    n_freq_df['maf_zim'] = ((n_freq_df['maf_ZH'] * n_freq_df['n_ZH']) + (n_freq_df['maf_ZW'] * n_freq_df['n_ZW']) * (n_freq_df['maf_ZS'] * n_freq_df['n_ZS'])) / n_freq_df['n_zim']


    print('new dataframe made for ' + infile)

    #create csv file
    number = infile.split("_")[3]

    n_freq_df.to_csv('downsampled_allele_freq_chunk{num}.csv'.format(num=number), index=False)

    print('new file made from ' + infile)




#for parallele mapping
csv_list = []

#run in parallel
def run_in_parallel():
    pool = Pool(processes=8)
    pool.map(snp_csv_downsample, csv_list)


if __name__ == '__main__':
    run_in_parallel()





