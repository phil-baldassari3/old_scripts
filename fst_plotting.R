library(ggplot2)
library(dplyr)
library(tidyr)

#set directory
setwd("/Users/philipbaldassari/Desktop/zim-cos_popgen/fst/windowed_fst_csv")

#reading files
FR.fst_ChrX <- read.csv("zim.vs.FR_ChrX.fst.csv")
head(FR.fst_ChrX)
FR.fst_Chr2L <- read.csv("zim.vs.FR_Chr2L.fst.csv")
FR.fst_Chr2R <- read.csv("zim.vs.FR_Chr2R.fst.csv")
FR.fst_Chr3L <- read.csv("zim.vs.FR_Chr3L.fst.csv")
FR.fst_Chr3R <- read.csv("zim.vs.FR_Chr3R.fst.csv")

RAL.fst_ChrX <- read.csv("zim.vs.RAL_ChrX.fst.csv")
head(RAL.fst_ChrX)
RAL.fst_Chr2L <- read.csv("zim.vs.RAL_Chr2L.fst.csv")
RAL.fst_Chr2R <- read.csv("zim.vs.RAL_Chr2R.fst.csv")
RAL.fst_Chr3L <- read.csv("zim.vs.RAL_Chr3L.fst.csv")
RAL.fst_Chr3R <- read.csv("zim.vs.RAL_Chr3R.fst.csv")

SA.fst_ChrX <- read.csv("zim.vs.SAfr_ChrX.fst.csv")
head(SA.fst_ChrX)
SA.fst_Chr2L <- read.csv("zim.vs.SAfr_Chr2L.fst.csv")
SA.fst_Chr2R <- read.csv("zim.vs.SAfr_Chr2R.fst.csv")
SA.fst_Chr3L <- read.csv("zim.vs.SAfr_Chr3L.fst.csv")
SA.fst_Chr3R <- read.csv("zim.vs.SAfr_Chr3R.fst.csv")

ZI.fst_ChrX <- read.csv("zim.vs.ZI_ChrX.fst.csv")
head(ZI.fst_ChrX)
ZI.fst_Chr2L <- read.csv("zim.vs.ZI_Chr2L.fst.csv")
ZI.fst_Chr2R <- read.csv("zim.vs.ZI_Chr2R.fst.csv")
ZI.fst_Chr3L <- read.csv("zim.vs.ZI_Chr3L.fst.csv")
ZI.fst_Chr3R <- read.csv("zim.vs.ZI_Chr3R.fst.csv")

zim.fst_ChrX <- read.csv("zim.vs.zim_ChrX.fst.csv")
zim.fst_Chr2L <- read.csv("zim.vs.zim_Chr2L.fst.csv")
zim.fst_Chr2R <- read.csv("zim.vs.zim_Chr2R.fst.csv")
zim.fst_Chr3L <- read.csv("zim.vs.zim_Chr3L.fst.csv")
zim.fst_Chr3R <- read.csv("zim.vs.zim_Chr3R.fst.csv")

#plot ChrX
ggplot() + geom_line(data=FR.fst_ChrX, aes(x=FR.fst_ChrX$BIN_START, y = FR.fst_ChrX$MEAN_FST, color = "zim vs. FR"), linetype="dotted") + 
  geom_line(data=RAL.fst_ChrX, aes(x=RAL.fst_ChrX$BIN_START, y = RAL.fst_ChrX$MEAN_FST, color = "zim vs. RAL"), linetype="dotted")  +
  geom_line(data=SA.fst_ChrX, aes(x=SA.fst_ChrX$BIN_START, y = SA.fst_ChrX$MEAN_FST, color = "zim vs. SAfr"), linetype="dotted")  +
  geom_line(data=ZI.fst_ChrX, aes(x=ZI.fst_ChrX$BIN_START, y = ZI.fst_ChrX$MEAN_FST, color = "zim vs. ZI"), linetype="dotted") +
  geom_line(data=zim.fst_ChrX, aes(x=zim.fst_ChrX$BIN_START, y = zim.fst_ChrX$MEAN_FST, color = "zim vs. zim"), linetype="dotted") +
  xlab(" ") + ylab("Mean Fst") + ggtitle("ChrX Fst (10kbp sliding window)") + labs(colour=' ')
 
#plot Chr2L
ggplot() + geom_line(data=FR.fst_Chr2L, aes(x=FR.fst_Chr2L$BIN_START, y = FR.fst_Chr2L$MEAN_FST, color = "zim vs. FR"), linetype="dotted") + 
  geom_line(data=RAL.fst_Chr2L, aes(x=RAL.fst_Chr2L$BIN_START, y = RAL.fst_Chr2L$MEAN_FST, color = "zim vs. RAL"), linetype="dotted")  +
  geom_line(data=SA.fst_Chr2L, aes(x=SA.fst_Chr2L$BIN_START, y = SA.fst_Chr2L$MEAN_FST, color = "zim vs. SAfr"), linetype="dotted")  +
  geom_line(data=ZI.fst_Chr2L, aes(x=ZI.fst_Chr2L$BIN_START, y = ZI.fst_Chr2L$MEAN_FST, color = "zim vs. ZI"), linetype="dotted") +
  geom_line(data=zim.fst_Chr2L, aes(x=zim.fst_Chr2L$BIN_START, y = zim.fst_Chr2L$MEAN_FST, color = "zim vs. zim"), linetype="dotted") +
  xlab(" ") + ylab("Mean Fst") + ggtitle("Chr2L Fst (10kbp sliding window)") + labs(colour=' ')
#plot Chr2R
ggplot() + geom_line(data=FR.fst_Chr2R, aes(x=FR.fst_Chr2R$BIN_START, y = FR.fst_Chr2R$MEAN_FST, color = "zim vs. FR"), linetype="dotted") + 
  geom_line(data=RAL.fst_Chr2R, aes(x=RAL.fst_Chr2R$BIN_START, y = RAL.fst_Chr2R$MEAN_FST, color = "zim vs. RAL"), linetype="dotted")  +
  geom_line(data=SA.fst_Chr2R, aes(x=SA.fst_Chr2R$BIN_START, y = SA.fst_Chr2R$MEAN_FST, color = "zim vs. SAfr"), linetype="dotted")  +
  geom_line(data=ZI.fst_Chr2R, aes(x=ZI.fst_Chr2R$BIN_START, y = ZI.fst_Chr2R$MEAN_FST, color = "zim vs. ZI"), linetype="dotted") +
  geom_line(data=zim.fst_Chr2R, aes(x=zim.fst_Chr2R$BIN_START, y = zim.fst_Chr2R$MEAN_FST, color = "zim vs. zim"), linetype="dotted") +
  xlab(" ") + ylab("Mean Fst") + ggtitle("Chr2R Fst (10kbp sliding window)") + labs(colour=' ')
#plot Chr3L
ggplot() + geom_line(data=FR.fst_Chr3L, aes(x=FR.fst_Chr3L$BIN_START, y = FR.fst_Chr3L$MEAN_FST, color = "zim vs. FR"), linetype="dotted") + 
  geom_line(data=RAL.fst_Chr3L, aes(x=RAL.fst_Chr3L$BIN_START, y = RAL.fst_Chr3L$MEAN_FST, color = "zim vs. RAL"), linetype="dotted")  +
  geom_line(data=SA.fst_Chr3L, aes(x=SA.fst_Chr3L$BIN_START, y = SA.fst_Chr3L$MEAN_FST, color = "zim vs. SAfr"), linetype="dotted")  +
  geom_line(data=ZI.fst_Chr3L, aes(x=ZI.fst_Chr3L$BIN_START, y = ZI.fst_Chr3L$MEAN_FST, color = "zim vs. ZI"), linetype="dotted") +
  geom_line(data=zim.fst_Chr3L, aes(x=zim.fst_Chr3L$BIN_START, y = zim.fst_Chr3L$MEAN_FST, color = "zim vs. zim"), linetype="dotted") +
  xlab(" ") + ylab("Mean Fst") + ggtitle("Chr3L Fst (10kbp sliding window)") + labs(colour=' ')
#plot Chr3R
ggplot() + geom_line(data=FR.fst_Chr3R, aes(x=FR.fst_Chr3R$BIN_START, y = FR.fst_Chr3R$MEAN_FST, color = "zim vs. FR"), linetype="dotted") + 
  geom_line(data=RAL.fst_Chr3R, aes(x=RAL.fst_Chr3R$BIN_START, y = RAL.fst_Chr3R$MEAN_FST, color = "zim vs. RAL"), linetype="dotted")  +
  geom_line(data=SA.fst_Chr3R, aes(x=SA.fst_Chr3R$BIN_START, y = SA.fst_Chr3R$MEAN_FST, color = "zim vs. SAfr"), linetype="dotted")  +
  geom_line(data=ZI.fst_Chr3R, aes(x=ZI.fst_Chr3R$BIN_START, y = ZI.fst_Chr3R$MEAN_FST, color = "zim vs. ZI"), linetype="dotted") +
  geom_line(data=zim.fst_Chr3R, aes(x=zim.fst_Chr3R$BIN_START, y = zim.fst_Chr3R$MEAN_FST, color = "zim vs. zim"), linetype="dotted") +
  xlab(" ") + ylab("Mean Fst") + ggtitle("Chr3R Fst (10kbp sliding window)") + labs(colour=' ')

ggplot() + geom_line(data=ZI.fst_Chr3R, aes(x=ZI.fst_Chr3R$BIN_START, y = ZI.fst_Chr3R$MEAN_FST))

##Making one data frame for all data
#simplifying the dataframes
simp_RAL_ChrX <- RAL.fst_ChrX %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.RAL = MEAN_FST)
head(simp_RAL_ChrX)
simp_FR_ChrX <- FR.fst_ChrX %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.FR = MEAN_FST, BIN_END_FR = BIN_END, CHROM_FR = CHROM)
head(simp_FR_ChrX)
simp_ZI_ChrX <- ZI.fst_ChrX %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.ZI = MEAN_FST, BIN_END_ZI = BIN_END, CHROM_ZI = CHROM)
simp_SA_ChrX <- SA.fst_ChrX %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.SA = MEAN_FST, BIN_END_SA = BIN_END, CHROM_SA = CHROM)

simp_RAL_Chr2L <- RAL.fst_Chr2L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.RAL = MEAN_FST)
simp_FR_Chr2L <- FR.fst_Chr2L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.FR = MEAN_FST, BIN_END_FR = BIN_END, CHROM_FR = CHROM)
simp_ZI_Chr2L <- ZI.fst_Chr2L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.ZI = MEAN_FST, BIN_END_ZI = BIN_END, CHROM_ZI = CHROM)
simp_SA_Chr2L <- SA.fst_Chr2L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.SA = MEAN_FST, BIN_END_SA = BIN_END, CHROM_SA = CHROM)

simp_RAL_Chr2R <- RAL.fst_Chr2R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.RAL = MEAN_FST)
simp_FR_Chr2R <- FR.fst_Chr2R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.FR = MEAN_FST, BIN_END_FR = BIN_END, CHROM_FR = CHROM)
simp_ZI_Chr2R <- ZI.fst_Chr2R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.ZI = MEAN_FST, BIN_END_ZI = BIN_END, CHROM_ZI = CHROM)
simp_SA_Chr2R <- SA.fst_Chr2R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.SA = MEAN_FST, BIN_END_SA = BIN_END, CHROM_SA = CHROM)

simp_RAL_Chr3L <- RAL.fst_Chr3L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.RAL = MEAN_FST)
simp_FR_Chr3L <- FR.fst_Chr3L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.FR = MEAN_FST, BIN_END_FR = BIN_END, CHROM_FR = CHROM)
simp_ZI_Chr3L <- ZI.fst_Chr3L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.ZI = MEAN_FST, BIN_END_ZI = BIN_END, CHROM_ZI = CHROM)
simp_SA_Chr3L <- SA.fst_Chr3L %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.SA = MEAN_FST, BIN_END_SA = BIN_END, CHROM_SA = CHROM)

simp_RAL_Chr3R <- RAL.fst_Chr3R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.RAL = MEAN_FST)
simp_FR_Chr3R <- FR.fst_Chr3R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.FR = MEAN_FST, BIN_END_FR = BIN_END, CHROM_FR = CHROM)
simp_ZI_Chr3R <- ZI.fst_Chr3R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.ZI = MEAN_FST, BIN_END_ZI = BIN_END, CHROM_ZI = CHROM)
simp_SA_Chr3R <- SA.fst_Chr3R %>%
  select(-N_VARIANTS, -WEIGHTED_FST) %>%
  rename(MEAN_FST_zim.v.SA = MEAN_FST, BIN_END_SA = BIN_END, CHROM_SA = CHROM)

#merging the dataframes
draft_ChrX_RAL_FR <- merge(simp_RAL_ChrX, simp_FR_ChrX, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_ChrX_zim_RAL)
draft_ChrX_RAL_FR_ZI <- merge(draft_ChrX_RAL_FR, simp_ZI_ChrX, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_ChrX_RAL_FR_ZI)
draft_ChrX <- merge(draft_ChrX_RAL_FR_ZI, simp_SA_ChrX, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_ChrX)

draft_Chr2L_RAL_FR <- merge(simp_RAL_Chr2L, simp_FR_Chr2L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr2L_RAL_FR_ZI <- merge(draft_Chr2L_RAL_FR, simp_ZI_Chr2L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr2L <- merge(draft_Chr2L_RAL_FR_ZI, simp_SA_Chr2L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_Chr2L)

draft_Chr2R_RAL_FR <- merge(simp_RAL_Chr2R, simp_FR_Chr2R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr2R_RAL_FR_ZI <- merge(draft_Chr2R_RAL_FR, simp_ZI_Chr2R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr2R <- merge(draft_Chr2R_RAL_FR_ZI, simp_SA_Chr2R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_Chr2R)

draft_Chr3L_RAL_FR <- merge(simp_RAL_Chr3L, simp_FR_Chr3L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr3L_RAL_FR_ZI <- merge(draft_Chr3L_RAL_FR, simp_ZI_Chr3L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr3L <- merge(draft_Chr3L_RAL_FR_ZI, simp_SA_Chr3L, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_Chr3L)

draft_Chr3R_RAL_FR <- merge(simp_RAL_Chr3R, simp_FR_Chr3R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr3R_RAL_FR_ZI <- merge(draft_Chr3R_RAL_FR, simp_ZI_Chr3R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
draft_Chr3R <- merge(draft_Chr3R_RAL_FR_ZI, simp_SA_Chr3R, by.x = "BIN_START", by.y = "BIN_START", all.x = TRUE)
head(draft_Chr3R)

#Finalizing the merged dataframes with averges
fst_ChrX <- draft_ChrX %>%
  select(-BIN_END_FR, -BIN_END_ZI, -BIN_END_SA, -CHROM_FR, -CHROM_ZI, -CHROM_SA) %>%
  mutate(AVG_FST = (MEAN_FST_zim.v.RAL + MEAN_FST_zim.v.FR + MEAN_FST_zim.v.ZI + MEAN_FST_zim.v.SA)/4)
head(fst_ChrX)
fst_Chr2L <- draft_Chr2L %>%
  select(-BIN_END_FR, -BIN_END_ZI, -BIN_END_SA, -CHROM_FR, -CHROM_ZI, -CHROM_SA) %>%
  mutate(AVG_FST = (MEAN_FST_zim.v.RAL + MEAN_FST_zim.v.FR + MEAN_FST_zim.v.ZI + MEAN_FST_zim.v.SA)/4)
head(fst_Chr2L)
fst_Chr2R <- draft_Chr2R %>%
  select(-BIN_END_FR, -BIN_END_ZI, -BIN_END_SA, -CHROM_FR, -CHROM_ZI, -CHROM_SA) %>%
  mutate(AVG_FST = (MEAN_FST_zim.v.RAL + MEAN_FST_zim.v.FR + MEAN_FST_zim.v.ZI + MEAN_FST_zim.v.SA)/4)
head(fst_Chr2R)
fst_Chr3L <- draft_Chr3L %>%
  select(-BIN_END_FR, -BIN_END_ZI, -BIN_END_SA, -CHROM_FR, -CHROM_ZI, -CHROM_SA) %>%
  mutate(AVG_FST = (MEAN_FST_zim.v.RAL + MEAN_FST_zim.v.FR + MEAN_FST_zim.v.ZI + MEAN_FST_zim.v.SA)/4)
head(fst_Chr3L)
fst_Chr3R <- draft_Chr3R %>%
  select(-BIN_END_FR, -BIN_END_ZI, -BIN_END_SA, -CHROM_FR, -CHROM_ZI, -CHROM_SA) %>%
  mutate(AVG_FST = (MEAN_FST_zim.v.RAL + MEAN_FST_zim.v.FR + MEAN_FST_zim.v.ZI + MEAN_FST_zim.v.SA)/4)
head(fst_Chr3R)
fst_Chr3R[1400:1500, ]

#plotting the averages
ggplot() + geom_line(data=fst_ChrX, aes(x=BIN_START, y = AVG_FST)) +
  xlab(" ") + ylab("Avg Fst") + ggtitle("ChrX Avg Fst zim vs. RAL, FR, ZI, SA")
ggplot() + geom_line(data=fst_Chr2L, aes(x=BIN_START, y = AVG_FST)) +
  xlab(" ") + ylab("Avg Fst") + ggtitle("Chr2L Avg Fst zim vs. RAL, FR, ZI, SA")
ggplot() + geom_line(data=fst_Chr2R, aes(x=BIN_START, y = AVG_FST)) +
  xlab(" ") + ylab("Avg Fst") + ggtitle("Chr2R Avg Fst zim vs. RAL, FR, ZI, SA")
ggplot() + geom_line(data=fst_Chr3L, aes(x=BIN_START, y = AVG_FST)) +
  xlab(" ") + ylab("Avg Fst") + ggtitle("Chr3L Avg Fst zim vs. RAL, FR, ZI, SA")
ggplot() + geom_line(data=fst_Chr3R, aes(x=BIN_START, y = AVG_FST)) +
  xlab(" ") + ylab("Avg Fst") + ggtitle("Chr3R Avg Fst zim vs. RAL, FR, ZI, SA")

#joining dataframes
Fst <- rbind(fst_ChrX, fst_Chr2L, fst_Chr2R, fst_Chr3L, fst_Chr3R)
arranged_fst <- Fst %>%
  arrange(desc(AVG_FST))

head(arranged_fst, n = 50)

############
#arranged dataframes without the ends of chromosomes
arranged_fst_ChrX <- fst_ChrX %>%
  filter(BIN_START <20000000) %>%
  filter(BIN_START >100000) %>%
  arrange(desc(AVG_FST))
arranged_fst_Chr2L <- fst_Chr2L %>%
  filter(BIN_START <20000000) %>%
  filter(BIN_START >100000) %>%
  arrange(desc(AVG_FST))
arranged_fst_Chr2R <- fst_Chr2R %>%
  filter(BIN_START <20000000) %>%
  filter(BIN_START >100000) %>%
  arrange(desc(AVG_FST))
arranged_fst_Chr3L <- fst_Chr3L %>%
  filter(BIN_START <20000000) %>%
  filter(BIN_START >100000) %>%
  arrange(desc(AVG_FST))
arranged_fst_Chr3R <- fst_Chr3R %>%
  filter(BIN_START <20000000) %>%
  filter(BIN_START >100000) %>%
  arrange(desc(MEAN_FST_zim.v.ZI))

head(arranged_fst_ChrX, n=10)
head(arranged_fst_Chr2L, n=10)
head(arranged_fst_Chr2R, n=10)
head(arranged_fst_Chr3L, n=10)
head(arranged_fst_Chr3R, n=10)
#############

#####################################################################################
#per site fst

setwd("/Users/philipbaldassari/Desktop/zim-cos_popgen/fst/persite_fst")

#converting tables to csv files ONLY DO THIS ONCE
#####################
FR_file <- read.delim("zim.vs.FR_persite.weir.fst")
write.table(FR_file,file="zim.vs.FR_persite.fst.csv",sep=",",col.names=TRUE,row.names=FALSE)

RAL_file <- read.delim("zim.vs.RAL_persite.weir.fst")
write.table(RAL_file,file="zim.vs.RAL_persite.fst.csv",sep=",",col.names=TRUE,row.names=FALSE)

ZI_file <- read.delim("zim.vs.ZI_persite.weir.fst")
write.table(ZI_file,file="zim.vs.ZI_persite.fst.csv",sep=",",col.names=TRUE,row.names=FALSE)

SA_file <- read.delim("zim.vs.SAfr_persite.weir.fst")
write.table(SA_file,file="zim.vs.SAfr_persite.fst.csv",sep=",",col.names=TRUE,row.names=FALSE)

zim_file <- read.delim("zim.vs.zim_persite.weir.fst")
write.table(zim_file,file="zim.vs.zim_persite.fst.csv",sep=",",col.names=TRUE,row.names=FALSE)
#####################

#opening csv files
FR.fst_persite <- read.csv("zim.vs.FR_persite.fst.csv")
head(FR.fst_persite)

RAL.fst_persite <- read.csv("zim.vs.RAL_persite.fst.csv")
head(RAL.fst_persite)

ZI.fst_persite <- read.csv("zim.vs.ZI_persite.fst.csv")
head(ZI.fst_persite)

SA.fst_persite <- read.csv("zim.vs.SAfr_persite.fst.csv")
head(SA.fst_persite)

zim.fst_persite <- read.csv("zim.vs.zim_persite.fst.csv")
head(zim.fst_persite)

##Making one data frame for all data

#renaming columns of the dataframes
rename_RAL.fst_persite <- RAL.fst_persite %>%
  rename(FST_zim.v.RAL = WEIR_AND_COCKERHAM_FST)
head(rename_RAL.fst_persite)

rename_FR.fst_persite <- FR.fst_persite %>%
  rename(FST_zim.v.FR = WEIR_AND_COCKERHAM_FST, CHROM_FR = CHROM)

rename_ZI.fst_persite <- ZI.fst_persite %>%
  rename(FST_zim.v.ZI = WEIR_AND_COCKERHAM_FST, CHROM_ZI = CHROM)
head(rename_ZI.fst_persite)
rename_SA.fst_persite <- SA.fst_persite %>%
  rename(FST_zim.v.SA = WEIR_AND_COCKERHAM_FST, CHROM_SA = CHROM)

rename_zim.fst_persite <- zim.fst_persite %>%
  rename(FST_zim.v.zim = WEIR_AND_COCKERHAM_FST,CHROM_zim = CHROM)

#merge dataframes
merged_RAL_FR <- merge(rename_RAL.fst_persite, rename_FR.fst_persite, by.x = "POS", by.y = "POS", all.x = TRUE)
head(merged_RAL_FR)
merged_RAL_FR_ZI <- merge(merged_RAL_FR, rename_ZI.fst_persite, by.x = "POS", by.y = "POS", all.x = TRUE)
head(merged_RAL_FR_ZI)
merged_RAL_FR_ZI_SA <- merge(merged_RAL_FR_ZI, rename_SA.fst_persite, by.x = "POS", by.y = "POS", all.x = TRUE)
head(merged_RAL_FR_ZI_SA)
draft_merged_fst_persite <- merge(merged_RAL_FR_ZI_SA, rename_zim.fst_persite, by.x = "POS", by.y = "POS", all.x = TRUE)
head(draft_merged_fst_persite)

#simplifying merged dataframes
simp_merged_fst_persite <- draft_merged_fst_persite %>%
  select(-CHROM_FR, -CHROM_ZI, -CHROM_SA, -CHROM_zim)
head(simp_merged_fst_persite)
simp_merged_fst_persite[1000:1020, ]

#averaging
fst_persite <- simp_merged_fst_persite %>%
  mutate(AVG_FST = (FST_zim.v.RAL + FST_zim.v.FR + FST_zim.v.ZI + FST_zim.v.SA)/4) %>%
  drop_na(AVG_FST)
head(fst_persite)

#separating chroms
fst_persite_ChrX <- fst_persite %>%
  filter(CHROM == "X")
head(fst_persite_ChrX)

fst_persite_ChrX <- fst_persite_ChrX %>%
  drop_na(AVG_FST)
head(fst_persite_ChrX)
####fst_persite_ChrX$AVG_FST[fst_persite_ChrX$AVG_FST <0]<- 0

fst_persite_Chr2L <- fst_persite %>%
  filter(CHROM == "2L") %>%
  drop_na(AVG_FST)
head(fst_persite_Chr2L)

fst_persite_Chr2R <- fst_persite %>%
  filter(CHROM == "2R") %>%
  drop_na(AVG_FST)
head(fst_persite_Chr2R)

fst_persite_Chr3L <- fst_persite %>%
  filter(CHROM == "3L") %>%
  drop_na(AVG_FST)
head(fst_persite_Chr3L)

fst_persite_Chr3R <- fst_persite %>%
  filter(CHROM == "3R") %>%
  drop_na(AVG_FST)
head(fst_persite_Chr3R)

#ploting the per site snps
#plotX <- ggplot(fst_persite_ChrX, aes(POS, AVG_FST)) +geom_point()  
#plotX


#finding highest fst values
arranged_fst_persite <- fst_persite %>%
  arrange(desc(AVG_FST))

arranged_fst_persite[1:300, ]

#z scores
fst_persite <- fst_persite %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

head(fst_persite, n=50)

#autosomes only
autosomes_fst_persite <- fst_persite %>%
  filter(CHROM != "X")
  
autosomes_fst_persite[1:100, ]
autosomes_fst_persite[100:200, ]
autosomes_fst_persite[200:300, ]

#Highest zscores by chrom
fst_persite_ChrX <- fst_persite_ChrX %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

fst_persite_Chr2L <- fst_persite_Chr2L %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

fst_persite_Chr2R <- fst_persite_Chr2R %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

fst_persite_Chr3L <- fst_persite_Chr3L %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

fst_persite_Chr3R <- fst_persite_Chr3R %>%
  mutate(zscore = (AVG_FST - mean(AVG_FST))/sd(AVG_FST)) %>%
  arrange(desc(zscore))

head(fst_persite_ChrX, n=20)
head(fst_persite_Chr2L, n=20)
head(fst_persite_Chr2R, n=20)
head(fst_persite_Chr3L, n=20)
head(fst_persite_Chr3R, n=20)

finding_fru <- fst_persite_Chr3R %>%
  filter(POS >= 4239995) %>%
  filter(POS <= 4371308) %>%
  mutate(AVG_OLD = (FST_zim.v.RAL+FST_zim.v.ZI)/2) #Average of zimvRAL and zimvZI ***some samples from zim were not included the first time but still are included here

finding_fru

fst_persite_wOLD <- fst_persite %>%
  mutate(AVG_OLD = (FST_zim.v.RAL+FST_zim.v.ZI)/2) %>%
  arrange(desc(AVG_OLD))

 
fst_persite_wOLD

autosomes_fst_persite_wOLD <- autosomes_fst_persite %>%
  mutate(AVG_OLD = (FST_zim.v.RAL+FST_zim.v.ZI)/2) %>%
  arrange(desc(AVG_OLD))


autosomes_fst_persite_wOLD


#density functions of Fst
density_fst <- density(fst_persite$AVG_FST)
plot(density_fst)
hist(fst_persite$AVG_FST)
RAL_den <- density(fst_persite$FST_zim.v.RAL)
plot(RAL_den)
FR_den <- density(fst_persite$FST_zim.v.FR)
plot(FR_den)
ZI_den <- density(fst_persite$FST_zim.v.ZI)
plot(ZI_den)
SA_den <- density(fst_persite$FST_zim.v.SA)
plot(SA_den)





