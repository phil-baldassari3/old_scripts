import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import upsetplot


#functions
def plot_upset_from_gene_csvs(csv_ls, plotname, subset="all"):
    """
    makes upset plot from lists of genes from the top gene csv files. A list of csv files is the first argument. The files will be opened and the gene lists extracted.
    Pass the title of the plot you wish to output as plotname
    subset is an optional argument if you would like to subset the gene lists by a specific paramenter of the dataframe. Pass the exact parameter name to subset
    Also returns a modified upset dataframe
    """

    gene_ls_dict = {}

    for i in csv_ls:

        #name of the set
        comparison_name = '_'.join(i.split('_')[2:]).replace('_Fst_ChrX.csv', '')   #BE CAREFUL WITH THIS!
        comparison_name = comparison_name.replace('_Fst_autosomes.csv', '')

        #opening and subseting df if necessary
        if subset == "all":
            df = pd.read_csv(i)
        else:
            full_df = pd.read_csv(i)
            df = full_df[full_df.apply(lambda row: row.astype(str).str.match(subset, case=False).any(), axis=1)]

        #updating dictionary
        gene_ls_dict.update({comparison_name: df["FBgn"].to_list()})


    #converting dictionary to upset format
    gene_sets = upsetplot.from_contents(gene_ls_dict)

    #plotting
    p = upsetplot.UpSet(gene_sets, subset_size='count', sort_by='-degree', sort_categories_by='-input').plot()
#sort_by='cardinality'
    plt.title(plotname)
    plt.savefig(plotname + '_upset.png')


    return gene_sets.reset_index()
    

        
def extract_subset(df, bool_ls):
    """
    Function takes a upset dataframe and a bool list defining the rows of the dataframe to select and returns a list of items of the seelcted subset
    Note that the bool list needs to be in the same order as the catagories passed to plot_upset_from_gene_csvs()
    """
    #find how many rows to subset from
    length = len(bool_ls)

    #getting subset
    subset_df = df.loc[(df.iloc[:, :length] == bool_ls).all(axis=1)]

    #getting list of genes
    subset_genes = subset_df['id'].to_list()

    return subset_genes


def extract_all_subsets(df, num_of_catagories):
    """Function takes in the upset dataframe and the number of categorites and outputs a dictionary of lists of all subsets"""

    #unique list of booleans that describe the identiy of each item in each catagory
    unique_bools = df.iloc[:, :num_of_catagories].drop_duplicates().values.tolist()

    subsets_dict = {}
    for i in unique_bools:
        subset = extract_subset(df, i)

        subsets_dict.update({str(i): subset})

    return subsets_dict






#csv lists
chrx = ['top1_genes_ZS_vs_RAL_ZI_Fst_ChrX.csv', 'top1_genes_ZS_vs_RAL_ZI_FR_SAfr_Fst_ChrX.csv', 'top1_genes_ZS_vs_ZH_ZW_Fst_ChrX.csv', 'top1_genes_ZH_vs_RAL_ZI_Fst_ChrX.csv', 'top1_genes_ZW_vs_RAL_ZI_Fst_ChrX.csv', 'top1_genes_RAL_vs_FR_ZI_SAfr_Fst_ChrX.csv', 'top1_genes_FR_vs_RAL_ZI_SAfr_Fst_ChrX.csv', 'top1_genes_ZI_vs_RAL_FR_SAfr_Fst_ChrX.csv', 'top1_genes_SAfr_vs_RAL_FR_ZI_Fst_ChrX.csv']
autosomes = ['top1_genes_ZS_vs_RAL_ZI_Fst_autosomes.csv', 'top1_genes_ZS_vs_RAL_ZI_FR_SAfr_Fst_autosomes.csv', 'top1_genes_ZS_vs_ZH_ZW_Fst_autosomes.csv', 'top1_genes_ZH_vs_RAL_ZI_Fst_autosomes.csv', 'top1_genes_ZW_vs_RAL_ZI_Fst_autosomes.csv', 'top1_genes_RAL_vs_FR_ZI_SAfr_Fst_autosomes.csv', 'top1_genes_FR_vs_RAL_ZI_SAfr_Fst_autosomes.csv', 'top1_genes_ZI_vs_RAL_FR_SAfr_Fst_autosomes.csv', 'top1_genes_SAfr_vs_RAL_FR_ZI_Fst_autosomes.csv']



#generating upset plots
chrx_all = plot_upset_from_gene_csvs(chrx, "Significanlty differentiated genes\nby per site Fst from ChromX")
chrx_neuro = plot_upset_from_gene_csvs(chrx, "Significanlty differentiated neurogenesis genes\nby per site Fst from ChromX", subset='Neurogenesis')
autosome_all = plot_upset_from_gene_csvs(autosomes, "Significanlty differentiated genes\nby per site Fst from Autosomes")
autosome_neuro = plot_upset_from_gene_csvs(autosomes, "Significanlty differentiated neurogenesis genes\nby per site Fst from Autosomes", subset='Neurogenesis')


#extracting subsets
zs = [True, True, True, False, False, False, False, False, False]
zim = [True, True, True, True, True, False, False, False, False]
zimNObn = [True, True, False, True, True, False, False, False, False]

zsX_all = extract_subset(chrx_all, zs)
zimX_all = extract_subset(chrx_all, zim)
zimNObnX_all = extract_subset(chrx_all, zimNObn)

zsX_neuro = extract_subset(chrx_neuro, zs)
zimX_neuro = extract_subset(chrx_neuro, zim)
zimNObnX_neuro = extract_subset(chrx_neuro, zimNObn)

zsA_all = extract_subset(autosome_all, zs)
zimA_all = extract_subset(autosome_all, zim)
zimNObnA_all = extract_subset(autosome_all, zimNObn)

zsA_neuro = extract_subset(autosome_neuro, zs)
zimA_neuro = extract_subset(autosome_neuro, zim)
zimNObnA_neuro = extract_subset(autosome_neuro, zimNObn)



#saving lists to files
with open("zsX_all.txt", 'w') as zsX_allfile:
    zsX_allfile.write('\n'.join(zsX_all))


with open("zimX_all.txt", 'w') as zimX_allfile:
    zimX_allfile.write('\n'.join(zimX_all))


with open("zimNObnX_all.txt", 'w') as zimNObnX_allfile:
    zimNObnX_allfile.write('\n'.join(zimNObnX_all))


with open("zsX_neuro.txt", 'w') as zsX_neurofile:
    zsX_neurofile.write('\n'.join(zsX_neuro))


with open("zimX_neuro.txt", 'w') as zimX_neurofile:
    zimX_neurofile.write('\n'.join(zimX_neuro))


with open("zimNObnX_neuro.txt", 'w') as zimNObnX_neurofile:
    zimNObnX_neurofile.write('\n'.join(zimNObnX_neuro))


with open("zsA_all.txt", 'w') as zsA_allfile:
    zsA_allfile.write('\n'.join(zsA_all))


with open("zimA_all.txt", 'w') as zimA_allfile:
    zimA_allfile.write('\n'.join(zimA_all))


with open("zimNObnA_all.txt", 'w') as zimNObnA_allfile:
    zimNObnA_allfile.write('\n'.join(zimNObnA_all))


with open("zsA_neuro.txt", 'w') as zsA_neurofile:
    zsA_neurofile.write('\n'.join(zsA_neuro))


with open("zimA_neuro.txt", 'w') as zimA_neurofile:
    zimA_neurofile.write('\n'.join(zimA_neuro))


with open("zimNObnA_neuro.txt", 'w') as zimNObnA_neurofile:
    zimNObnA_neurofile.write('\n'.join(zimNObnA_neuro))




