library(tidyverse)
library(ggmap)
library(ggplot2)
library(ape)
library(basetheme)
library(adegenet)
library(phangorn)


#setting directory
setwd("/Users/philipbaldassari/Desktop/zim_phylo")

##clustering alogrith by VCF-kit##

annot <- read.csv("subset_annot.csv", header=TRUE, row.names=1)
annot

#subset from zim, ZI, and RAL
zim.cos_nwk <- scan("subset_zim-cos_0.25.newick", what=character())
zim.cos_tree <- read.tree(text=zim.cos_nwk)
plot(zim.cos_tree,no.margin=TRUE,edge.width=0.5, cex=1)



##clustering alorithm by ape##


#Subset of zim_cos
#create DNAbin object
sub_zim.cos_dna <- fasta2DNAbin("subset_zim-cos_0.25.fa")
sub_zim.cos_dna

#distance matrix
sub_zim.cos_dist <- dist.dna(sub_zim.cos_dna, model = "TN93")
length(sub_zim.cos_dist)

sub_zim.cos_temp <- as.data.frame(as.matrix(sub_zim.cos_dist))
table.paint(sub_zim.cos_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

#make tree
sub_zim.cos_tree <- nj(sub_zim.cos_dist)
class(sub_zim.cos_tree)

sub_zim.cos_tree <- ladderize(sub_zim.cos_tree)
sub_zim.cos_tree

plot(sub_zim.cos_tree, cex = 1, tip.color = annot$Color, .color = annot$Color)
#plot(sub_zim.cos_tree, type = "unrooted", cex = 1, tip.color = annot$Color, .color = annot$Color)
legend("bottomleft", legend = unique(annot$POP), fill = unique(annot$Color))
title(main = c("\n", "Subset of zim-cos"))



