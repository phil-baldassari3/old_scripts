#importing modules
import os,sys
import numpy as np
import pandas as pd


#functions

def range_len(ls):
    """
    Function takes a list with two elements in it representing a range and returns the difference between the two.
    Used in find_overlaps() to select the smallest range.
    """

    length = ls[1] - ls[0] 

    return length



def find_overlaps(listoflists, winsize):
    """
    Function takes island lists and finds overlaps between all of them.
    The function takes a list of lists as listoflists, each sublist is an island list.
    The function also takes winsize which denotes the size of the windows to loop through (should match windows of your data).
    Returns a list of lists, each sublist represents a range.
    """

    #find the end
    totallist = [item for sublist in listoflists for item in sublist]

    if all(type(i) == float for i in totallist):
        return []
    else:
        end = max([max(sublist) for sublist in totallist if not np.isnan(sublist).any()])
        
        #loop through window starts and checking which ranges the window falls in
        #if there is one from each island list, the smallest range is appended to the results
        results = []

        for i in range(1,end,winsize):
            test = []

            for idx in range(len(listoflists)):
            
                #finding ranges at this i
                for j in range(len(listoflists[0])):
                    if not isinstance(listoflists[idx][j], float) and listoflists[idx][j][0] <= i and listoflists[idx][j][1] > i:
                        test.append(listoflists[idx][j])
                    elif isinstance(listoflists[idx][j], float):
                        break
                    else:
                        continue

            #if a range from each island list fits the i
            if len(test) == len(listoflists):

                #finding smallest range
                rangelen = float('inf')
                select = 0
                for i in range(len(test)):
                    check = range_len(test[i])
                    if check < rangelen:
                        rangelen = check
                        select = i
                    else:
                        continue

                #append the smallest range to result
                results.append(test[select])
            
            else:
                continue
                
                        
        #refining results
        new_results = []
        for i in results:
            if i not in new_results:
                new_results.append(i)
            else:
                continue


        return new_results




def main_func(islandsfile, namelist, window_size):
    """
    Function takes a list of pairwise comparison names, e.g. 'ZS.vs.RAL'. It opens the *islands.csv file given, and extracts lists based on the namelist given. The function must also take the window size.
    The fucntion then uses find_overlaps() to output a file of overlaps for that chromosome, for that comaprison.
    The list is saved as a file
    """

    #opening islands file
    islands = pd.read_csv(islandsfile)

    #extracting island lists for the chosen comparisons
    comparisons = {}

    for i in namelist:
        temp = islands[i].to_list()
        comparison_islands = [eval(j) if type(j) != float else j for j in temp]

        comparisons.update({i: comparison_islands})

    #finding overlaps
    lol = []
    for i in namelist:
        lol.append(comparisons[i])

    overlaps = find_overlaps(lol, window_size)
    overlaps_str = [str(i) for i in overlaps]

    #saving to file
    name = islandsfile
    name = name.replace("allcomparisons_", "")
    name = name.replace(".csv", "")

    with open("{n}_{c}.txt".format(n=name, c='_'.join(namelist)), 'w') as overlap_file:
        overlap_file.write('\n'.join(overlaps_str))









#main functions

main_func('win10kbp_ChrX_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI'], 10000)
main_func('win10kbp_ChrX_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI', 'ZS.vs.FR', 'ZS.vs.SAfr'], 10000)
main_func('win10kbp_ChrX_allcomparisons_islands.csv', ['ZH.vs.RAL', 'ZH.vs.ZI'], 10000)
main_func('win10kbp_ChrX_allcomparisons_islands.csv', ['ZW.vs.RAL', 'ZW.vs.ZI'], 10000)
main_func('win10kbp_ChrX_allcomparisons_islands.csv', ['RAL.vs.FR', 'RAL.vs.ZI', 'RAL.vs.SAfr'], 10000)


main_func('win10kbp_Chr2L_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI'], 10000)
main_func('win10kbp_Chr2L_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI', 'ZS.vs.FR', 'ZS.vs.SAfr'], 10000)
main_func('win10kbp_Chr2L_allcomparisons_islands.csv', ['ZH.vs.RAL', 'ZH.vs.ZI'], 10000)
main_func('win10kbp_Chr2L_allcomparisons_islands.csv', ['ZW.vs.RAL', 'ZW.vs.ZI'], 10000)
main_func('win10kbp_Chr2L_allcomparisons_islands.csv', ['RAL.vs.FR', 'RAL.vs.ZI', 'RAL.vs.SAfr'], 10000)


main_func('win10kbp_Chr2R_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI'], 10000)
main_func('win10kbp_Chr2R_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI', 'ZS.vs.FR', 'ZS.vs.SAfr'], 10000)
main_func('win10kbp_Chr2R_allcomparisons_islands.csv', ['ZH.vs.RAL', 'ZH.vs.ZI'], 10000)
main_func('win10kbp_Chr2R_allcomparisons_islands.csv', ['ZW.vs.RAL', 'ZW.vs.ZI'], 10000)
main_func('win10kbp_Chr2R_allcomparisons_islands.csv', ['RAL.vs.FR', 'RAL.vs.ZI', 'RAL.vs.SAfr'], 10000)


main_func('win10kbp_Chr3L_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI'], 10000)
main_func('win10kbp_Chr3L_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI', 'ZS.vs.FR', 'ZS.vs.SAfr'], 10000)
main_func('win10kbp_Chr3L_allcomparisons_islands.csv', ['ZH.vs.RAL', 'ZH.vs.ZI'], 10000)
main_func('win10kbp_Chr3L_allcomparisons_islands.csv', ['ZW.vs.RAL', 'ZW.vs.ZI'], 10000)
main_func('win10kbp_Chr3L_allcomparisons_islands.csv', ['RAL.vs.FR', 'RAL.vs.ZI', 'RAL.vs.SAfr'], 10000)


main_func('win10kbp_Chr3R_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI'], 10000)
main_func('win10kbp_Chr3R_allcomparisons_islands.csv', ['ZS.vs.RAL', 'ZS.vs.ZI', 'ZS.vs.FR', 'ZS.vs.SAfr'], 10000)
main_func('win10kbp_Chr3R_allcomparisons_islands.csv', ['ZH.vs.RAL', 'ZH.vs.ZI'], 10000)
main_func('win10kbp_Chr3R_allcomparisons_islands.csv', ['ZW.vs.RAL', 'ZW.vs.ZI'], 10000)
main_func('win10kbp_Chr3R_allcomparisons_islands.csv', ['RAL.vs.FR', 'RAL.vs.ZI', 'RAL.vs.SAfr'], 10000)









