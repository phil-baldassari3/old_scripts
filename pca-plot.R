#packages
library(SNPRelate)
library(ggplot2)
library(dplyr)

#setting directory
setwd("path/to/directory/with/vcf/or/gds")

#convert vcf to gds (ONLY DO THIS ONCE)
snpgdsVCF2GDS('file.vcf', 'file.gds', method=c("biallelic.only", "copy.num.of.ref"), snpfirstdim=FALSE, compress.annotation="ZIP_RA.max", compress.geno="", ref.allele=NULL, ignore.chr.prefix="chr", verbose=TRUE)

gds <- snpgdsOpen('file.gds')
snpgdsSummary(gds, show=TRUE)


#pca (ONLY DO ONCE)
pca <- snpgdsPCA(gds, sample.id=NULL, snp.id=NULL, autosome.only=FALSE)

#%variance for axes
variance <- pca$varprop*100
rounded_percent <- round(variance, 2)
head(variance)
head(rounded_percent)

#population info
poptxt <- scan("pop.txt", what=character())
head(poptxt)

#make pca data frame
tab <- data.frame(sample.id = pca$sample.id,
                  Population = poptxt,
                  EV1 = pca$eigenvect[,1],    # the first eigenvector
                  EV2 = pca$eigenvect[,2],    # the second eigenvector
                  stringsAsFactors = FALSE)

head(tab)

###plotting and formatting

#axis labels
xlab <- paste("EV2 (", toString(rounded_percent[2]), "% Variance)", sep="")
ylab <- paste("EV1 (", toString(rounded_percent[1]), "% Variance)", sep="")

xlab
ylab

#scatterplot
ggplot(tab, aes(EV2, EV1, colour=Population)) +geom_point(shape=19, size=2) +xlab(xlab) +ylab(ylab)

#if you need to filter to only see specific populations
just_african <- tab %>%
  filter(!(Population == "popcode1"), !(Population == "popcode2"))

ggplot(just_african, aes(EV2, EV1, colour=Population)) +geom_point(shape=19, size=2) +xlab(xlab) +ylab(ylab)




