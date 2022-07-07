import os
import itertools
import pandas as pd

directory = '/Users/philipbaldassari/Desktop/zim-cos_Chr3R/'

#creating a dictionary for file names and sequences
data = {}
for file in os.listdir(directory):
    if file.endswith('.seq'):
        #opening and reading seq file
        data[file.split('_')[0]] = open(file, 'r').read()
        
    else:
        continue       

print(data.keys())
 
#creating data frames for each population which will be merged later after operations are performed

#df for zim
print("Making zim dataframe.  Looping through zim data and performing calculations.  Please wait...")

df_zim = pd.DataFrame(columns = ["Locus", "Prop_tot_zim", "Aprop_zim", "Tprop_zim", "Cprop_zim", "Gprop_zim"])

site_zim = 0

for locus in zip(data.get("ZS10"), data.get("ZS11"), data.get("ZS37"), data.get("ZS5"), data.get("ZS56")):

    
    site_zim += 1
    
    Acount_zim = locus.count("A")
    Tcount_zim = locus.count("T")
    Ccount_zim = locus.count("C")
    Gcount_zim = locus.count("G")

    bpcount_zim = Acount_zim + Tcount_zim + Ccount_zim + Gcount_zim
    
    if bpcount_zim == 0:
        bpcount_zim += 1
    else:
        bpcount_zim == bpcount_zim
        
    Aprop_zim = Acount_zim / bpcount_zim
    Tprop_zim = Tcount_zim / bpcount_zim
    Cprop_zim = Ccount_zim / bpcount_zim
    Gprop_zim = Gcount_zim / bpcount_zim

    prop_tot_zim = Aprop_zim + Tprop_zim + Cprop_zim + Gprop_zim
    
    df_zim = df_zim.append({'Locus' : site_zim, 'Prop_tot_zim' : prop_tot_zim,  'Aprop_zim' : Aprop_zim, 'Tprop_zim' : Tprop_zim, 'Cprop_zim' : Cprop_zim, 'Gprop_zim' : Gprop_zim}, 
                ignore_index = True)

print("Done creating zim dataframe.  Continuing...")

#df for RAL

print("Making RAL dataframe.  Looping through zim data and performing calculations.  Please wait...")

df_RAL = pd.DataFrame(columns = ["Locus", "Prop_tot_RAL", "Aprop_RAL", "Tprop_RAL", "Cprop_RAL", "Gprop_RAL"])

site_RAL = 0

for locus in zip(data.get("RAL-100"), data.get("RAL-101"), data.get("RAL-105"), data.get("RAL-109"), data.get("RAL-129"), data.get("RAL-136"), data.get("RAL-138"), data.get("RAL-142"), data.get("RAL-149"), data.get("RAL-153"), data.get("RAL-158"), data.get("RAL-161"), data.get("RAL-176"), data.get("RAL-177"), data.get("RAL-181"), data.get("RAL-189"), data.get("RAL-195"), data.get("RAL-208"), data.get("RAL-21"), data.get("RAL-217"), data.get("RAL-223"), data.get("RAL-227"), data.get("RAL-228"), data.get("RAL-229"), data.get("RAL-233"), data.get("RAL-235"), data.get("RAL-237"), data.get("RAL-239"), data.get("RAL-256"), data.get("RAL-26"), data.get("RAL-28"), data.get("RAL-280"), data.get("RAL-287"), data.get("RAL-301"), data.get("RAL-303"), data.get("RAL-304"), data.get("RAL-306"), data.get("RAL-307"), data.get("RAL-309"), data.get("RAL-31"), data.get("RAL-310"), data.get("RAL-313"), data.get("RAL-315"), data.get("RAL-317"), data.get("RAL-318"), data.get("RAL-319"), data.get("RAL-32"), data.get("RAL-320"), data.get("RAL-321"), data.get("RAL-324"), data.get("RAL-325"), data.get("RAL-332"), data.get("RAL-335"), data.get("RAL-336"), data.get("RAL-338"), data.get("RAL-340"), data.get("RAL-348"), data.get("RAL-350"), data.get("RAL-352"), data.get("RAL-354"), data.get("RAL-355"), data.get("RAL-356"), data.get("RAL-357"), data.get("RAL-358"), data.get("RAL-359"), data.get("RAL-360"), data.get("RAL-361"), data.get("RAL-362"), data.get("RAL-365"), data.get("RAL-367"), data.get("RAL-370"), data.get("RAL-371"), data.get("RAL-373"), data.get("RAL-374"), data.get("RAL-375"), data.get("RAL-377"), data.get("RAL-379"), data.get("RAL-38"), data.get("RAL-380"), data.get("RAL-381"), data.get("RAL-382"), data.get("RAL-383"), data.get("RAL-385"), data.get("RAL-386"), data.get("RAL-390"), data.get("RAL-391"), data.get("RAL-392"), data.get("RAL-395"), data.get("RAL-397"), data.get("RAL-399"), data.get("RAL-40"), data.get("RAL-405"), data.get("RAL-406"), data.get("RAL-409"), data.get("RAL-41"), data.get("RAL-42"), data.get("RAL-426"), data.get("RAL-427"), data.get("RAL-437"), data.get("RAL-439"), data.get("RAL-440"), data.get("RAL-441"), data.get("RAL-443"), data.get("RAL-45"), data.get("RAL-461"), data.get("RAL-48"), data.get("RAL-486"), data.get("RAL-49"), data.get("RAL-491"), data.get("RAL-492"), data.get("RAL-502"), data.get("RAL-505"), data.get("RAL-508"), data.get("RAL-509"), data.get("RAL-513"), data.get("RAL-517"), data.get("RAL-528"), data.get("RAL-530"), data.get("RAL-531"), data.get("RAL-535"), data.get("RAL-551"), data.get("RAL-555"), data.get("RAL-559"), data.get("RAL-563"), data.get("RAL-566"), data.get("RAL-57"), data.get("RAL-584"), data.get("RAL-589"), data.get("RAL-59"), data.get("RAL-595"), data.get("RAL-596"), data.get("RAL-627"), data.get("RAL-630"), data.get("RAL-634"), data.get("RAL-639"), data.get("RAL-642"), data.get("RAL-646"), data.get("RAL-69"), data.get("RAL-703"), data.get("RAL-705"), data.get("RAL-707"), data.get("RAL-712"), data.get("RAL-714"), data.get("RAL-716"), data.get("RAL-721"), data.get("RAL-727"), data.get("RAL-73"), data.get("RAL-730"), data.get("RAL-732"), data.get("RAL-737"), data.get("RAL-738"), data.get("RAL-748"), data.get("RAL-75"), data.get("RAL-757"), data.get("RAL-761"), data.get("RAL-765"), data.get("RAL-774"), data.get("RAL-776"), data.get("RAL-783"), data.get("RAL-786"), data.get("RAL-787"), data.get("RAL-790"), data.get("RAL-796"), data.get("RAL-799"), data.get("RAL-801"), data.get("RAL-802"), data.get("RAL-804"), data.get("RAL-805"), data.get("RAL-808"), data.get("RAL-810"), data.get("RAL-812"), data.get("RAL-818"), data.get("RAL-819"), data.get("RAL-820"), data.get("RAL-821"), data.get("RAL-822"), data.get("RAL-83"), data.get("RAL-832"), data.get("RAL-837"), data.get("RAL-843"), data.get("RAL-849"), data.get("RAL-85"), data.get("RAL-850"), data.get("RAL-852"), data.get("RAL-853"), data.get("RAL-855"), data.get("RAL-857"), data.get("RAL-859"), data.get("RAL-861"), data.get("RAL-879"), data.get("RAL-88"), data.get("RAL-882"), data.get("RAL-884"), data.get("RAL-887"), data.get("RAL-890"), data.get("RAL-892"), data.get("RAL-894"), data.get("RAL-897"), data.get("RAL-900"), data.get("RAL-907"), data.get("RAL-908"), data.get("RAL-91"), data.get("RAL-911"), data.get("RAL-913"), data.get("RAL-93")):
    
    site_RAL += 1
    
    Acount_RAL = locus.count("A")
    Tcount_RAL = locus.count("T")
    Ccount_RAL = locus.count("C")
    Gcount_RAL = locus.count("G")
    
    bpcount_RAL = Acount_RAL + Tcount_RAL + Ccount_RAL + Gcount_RAL
    
    if bpcount_RAL == 0:
        bpcount_RAL += 1
    else:
        bpcount_RAL == bpcount_RAL
        
    Aprop_RAL = Acount_RAL / bpcount_RAL
    Tprop_RAL = Tcount_RAL / bpcount_RAL
    Cprop_RAL = Ccount_RAL / bpcount_RAL
    Gprop_RAL = Gcount_RAL / bpcount_RAL

    prop_tot_RAL = Aprop_RAL + Tprop_RAL + Cprop_RAL + Gprop_RAL
    
    df_RAL = df_RAL.append({'Locus' : site_RAL , 'Prop_tot_RAL' : prop_tot_RAL, 'Aprop_RAL' : Aprop_RAL, 'Tprop_RAL' : Tprop_RAL, 'Cprop_RAL' : Cprop_RAL, 'Gprop_RAL' : Gprop_RAL}, 
                ignore_index = True)

print("Done creating RAL dataframe.  Continuing...")

(
#combining the dataframes to perform difference score calculations. Merges based on locus

print("Merging dataframes bases on locus.  Please wait for difference score calculations to be performed...")

combined = pd.merge(df_zim, df_RAL, on='Locus')

combined['Adiff'] = abs(combined['Aprop_zim'] - combined['Aprop_RAL'])
combined['Tdiff'] = abs(combined['Tprop_zim'] - combined['Tprop_RAL'])
combined['Cdiff'] = abs(combined['Cprop_zim'] - combined['Cprop_RAL'])
combined['Gdiff'] = abs(combined['Gprop_zim'] - combined['Gprop_RAL'])

combined['diff_score'] = combined[["Adiff","Tdiff","Cdiff","Gdiff"]].max(axis=1)

nomissing_zim = combined[combined.Prop_tot_zim !=0]
nomissing_RAL = nomissing_zim[nomissing_zim.Prop_tot_RAL !=0]

#filtering put all sites with difference score of zero meaning monomorphic site

print("Filtering out monomorphic sites.  Please wait...")

filtered = nomissing_RAL[nomissing_RAL.diff_score !=0]


print("Done!")

print(filtered)

