library(ape)
library(adegenet)
library(phangorn)
library(ggmap)
library(basetheme)

#setting directory
setwd("/Users/philipbaldassari/Desktop/zim-cos_phylo")

#annotation files
annot1 <- read.csv("subset_annot1.csv", header=TRUE, row.names=1)
annot1

annot2 <- read.csv("subset_annot2.csv", header=TRUE, row.names=1)
annot2

annot3 <- read.csv("subset_annot3.csv", header=TRUE, row.names=1)
annot3

zim_annot <- read.csv("zim_annot.csv", header=TRUE, row.names=1)
zim_annot

#create DNAbin objects
sub1_dna <- fasta2DNAbin("subset1.fa")
sub1_dna

sub2_dna <- fasta2DNAbin("subset2.fa")
sub2_dna

sub3_dna <- fasta2DNAbin("subset3.fa")
sub3_dna

zim_dna <- fasta2DNAbin("zim_0.25.fa")
zim_dna

#distance matrices
sub1_dist <- dist.dna(sub1_dna, model = "TN93")
length(sub1_dist)
sub1_temp <- as.data.frame(as.matrix(sub1_dist))
table.paint(sub1_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

sub2_dist <- dist.dna(sub2_dna, model = "TN93")
length(sub2_dist)
sub2_temp <- as.data.frame(as.matrix(sub2_dist))
table.paint(sub2_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

sub3_dist <- dist.dna(sub3_dna, model = "TN93")
length(sub3_dist)
sub3_temp <- as.data.frame(as.matrix(sub3_dist))
table.paint(sub3_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

zim_dist <- dist.dna(zim_dna, model = "TN93")
length(zim_dist)
zim_temp <- as.data.frame(as.matrix(zim_dist))
table.paint(zim_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

#make trees
sub1_tree <- nj(sub1_dist)
class(sub1_tree)
sub1_tree <- ladderize(sub1_tree)
sub1_tree
plot(sub1_tree, cex = 1, tip.color = annot1$Color, .color = annot1$Color)
legend("bottomleft", legend = unique(annot1$POP), fill = unique(annot1$Color))
title(main = c("\n", "Subset of zim-cos #1"))

sub2_tree <- nj(sub2_dist)
class(sub2_tree)
sub2_tree <- ladderize(sub2_tree)
sub2_tree
plot(sub2_tree, cex = 1, tip.color = annot2$Color, .color = annot2$Color)
legend("bottomleft", legend = unique(annot2$POP), fill = unique(annot2$Color))
title(main = c("\n", "Subset of zim-cos #2"))

sub3_tree <- nj(sub3_dist)
class(sub3_tree)
sub3_tree <- ladderize(sub3_tree)
sub3_tree
plot(sub3_tree, cex = 1, tip.color = annot3$Color, .color = annot3$Color)
legend("bottomleft", legend = unique(annot3$POP), fill = unique(annot3$Color))
title(main = c("\n", "Subset of zim-cos #3"))

zim_tree <- njs(zim_dist)
class(zim_tree)
zim_tree <- ladderize(zim_tree)
zim_tree
plot(zim_tree, cex = 1, tip.color = zim_annot$Color, .color = zim_annot$Color)
legend("bottomleft", legend = unique(zim_annot$POP), fill = unique(zim_annot$Color))
title(main = c("\n", "Zim"))
















