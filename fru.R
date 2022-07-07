library(SNPRelate)
library(ggplot2)
library(ape)
library(apex)
library(adegenet)
library(pegas)
library(mmod)
library(poppr)

#setting directory
setwd("/Users/philipbaldassari/Desktop/fru")

# fasta plot
fru_dna <- read.multiFASTA("fru.fa")
#plot(fru_dna, cex = 0.2)

#PCA
#####ONLY DO ONCE
snpgdsVCF2GDS('fru_0.05.vcf', 'fru_0.05.gds', method=("biallelic.only"), snpfirstdim=FALSE, compress.annotation="ZIP_RA.max", compress.geno="", ref.allele=NULL, ignore.chr.prefix="chr", verbose=TRUE)
#####

gds_fru <- snpgdsOpen('fru_0.05.gds')
snpgdsSummary(gds_fru, show=TRUE)

pca_fru <- snpgdsPCA(gds_fru, sample.id=NULL, snp.id=NULL, autosome.only=FALSE)

var_fru <- pca_fru$varprop*100
rounded_fru <- round(var_fru, 2)
head(var_fru)
head(rounded_fru)

poptxt <- scan("zim-cos_pop.txt", what=character())
head(poptxt)

tab_fru <- data.frame(sample.id = pca_fru$sample.id,
                      Population = poptxt,
                      EV1 = pca_fru$eigenvect[,1],    # the first eigenvector
                      EV2 = pca_fru$eigenvect[,2],    # the second eigenvector
                      stringsAsFactors = FALSE)

head(tab_fru)

xlabfru <- paste("EV2 (", toString(rounded_fru[2]), "% Variance)", sep="")
ylabfru <- paste("EV1 (", toString(rounded_fru[1]), "% Variance)", sep="")
xlabfru
ylabfru

ggplot(tab_fru, aes(EV2, EV1, colour=Population)) +geom_point(shape=19, size=2) +xlab(xlabfru) +ylab(ylabfru) +ggtitle("Fru (minor alleles filtered 5%)") 

#Trees
annot1 <- read.csv("subset_annot1.csv", header=TRUE, row.names=1)
annot1

annot2 <- read.csv("subset_annot2.csv", header=TRUE, row.names=1)
annot2

annot3 <- read.csv("subset_annot3.csv", header=TRUE, row.names=1)
annot3

#create DNAbin objects
fru_sub1_dna <- fasta2DNAbin("fru_subset1.fa")
fru_sub1_dna

fru_sub2_dna <- fasta2DNAbin("fru_subset2.fa")
fru_sub2_dna

fru_sub3_dna <- fasta2DNAbin("fru_subset3.fa")
fru_sub3_dna

#distance matrices
fru_sub1_dist <- dist.dna(fru_sub1_dna, model = "TN93")
length(fru_sub1_dist)
fru_sub1_temp <- as.data.frame(as.matrix(fru_sub1_dist))
table.paint(fru_sub1_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

fru_sub2_dist <- dist.dna(fru_sub2_dna, model = "TN93")
length(fru_sub2_dist)
fru_sub2_temp <- as.data.frame(as.matrix(fru_sub2_dist))
table.paint(fru_sub2_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

fru_sub3_dist <- dist.dna(fru_sub3_dna, model = "TN93")
length(fru_sub3_dist)
fru_sub3_temp <- as.data.frame(as.matrix(fru_sub3_dist))
table.paint(fru_sub3_temp, cleg=0, clabel.row=.5, clabel.col=.5) #darker shades of gray mean a larger distance # you can also make cool color plots but they're much more complicated because they use the image() function

#make trees
fru_sub1_tree <- nj(fru_sub1_dist)
class(fru_sub1_tree)
fru_sub1_tree <- ladderize(fru_sub1_tree)
fru_sub1_tree
plot(fru_sub1_tree, cex = 1, tip.color = annot1$Color, .color = annot1$Color)
legend("bottomleft", legend = unique(annot1$POP), fill = unique(annot1$Color))
title(main = c("\n", "fru, Subset of zim-cos #1"))

fru_sub2_tree <- nj(fru_sub2_dist)
class(fru_sub2_tree)
fru_sub2_tree <- ladderize(fru_sub2_tree)
fru_sub2_tree
plot(fru_sub2_tree, cex = 1, tip.color = annot2$Color, .color = annot2$Color)
legend("bottomleft", legend = unique(annot2$POP), fill = unique(annot2$Color))
title(main = c("\n", "fru, Subset of zim-cos #2"))

fru_sub3_tree <- nj(fru_sub3_dist)
class(fru_sub3_tree)
fru_sub3_tree <- ladderize(fru_sub3_tree)
fru_sub3_tree
plot(fru_sub3_tree, cex = 1, tip.color = annot3$Color, .color = annot3$Color)
legend("bottomleft", legend = unique(annot3$POP), fill = unique(annot3$Color))
title(main = c("\n", "fru, Subset of zim-cos #3"))









#####no FR



#PCA
#####ONLY DO ONCE
snpgdsVCF2GDS('fru_noFR_0.05.vcf', 'fru_noFR_0.05.gds', method=("biallelic.only"), snpfirstdim=FALSE, compress.annotation="ZIP_RA.max", compress.geno="", ref.allele=NULL, ignore.chr.prefix="chr", verbose=TRUE)
#####

noFR_gds_fru <- snpgdsOpen('fru_noFR_0.05.gds')
snpgdsSummary(noFR_gds_fru, show=TRUE)

noFR_pca_fru <- snpgdsPCA(noFR_gds_fru, sample.id=NULL, snp.id=NULL, autosome.only=FALSE)

noFR_var_fru <- noFR_pca_fru$varprop*100
noFR_rounded_fru <- round(noFR_var_fru, 2)
head(noFR_var_fru)
head(noFR_rounded_fru)

noFR_poptxt <- scan("noFR.txt", what=character())
head(noFR_poptxt)

noFR_tab_fru <- data.frame(sample.id = noFR_pca_fru$sample.id,
                      Population = noFR_poptxt,
                      EV1 = noFR_pca_fru$eigenvect[,1],    # the first eigenvector
                      EV2 = noFR_pca_fru$eigenvect[,2],    # the second eigenvector
                      stringsAsFactors = FALSE)

head(noFR_tab_fru)

noFR_xlabfru <- paste("EV2 (", toString(rounded_fru[2]), "% Variance)", sep="")
noFR_ylabfru <- paste("EV1 (", toString(rounded_fru[1]), "% Variance)", sep="")
noFR_xlabfru
noFR_ylabfru

ggplot(noFR_tab_fru, aes(EV2, EV1, colour=Population)) +geom_point(shape=19, size=2) +xlab(xlabfru) +ylab(ylabfru) +ggtitle("Fru (minor alleles filtered 5%)") 



