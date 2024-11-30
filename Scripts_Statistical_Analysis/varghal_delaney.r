#!/usr/bin/env Rscript

# Explanation of results: https://rdrr.io/cran/rcompanion/man/vda.html
# How to use the vd.a function https://search.r-project.org/CRAN/refmans/effsize/html/VD.A.html

#install.packages("effsize")
library(effsize)

group1 <- c(89.46, 84.17, 90.46, 89.75, 89.53) #Baseline-S1
group2 <- c(73.3, 68.12, 69.35, 59.12, 77.30) #S1
group3 <- c(92.22,90.72,89.68,84.33,90.92) #Baseline-S2
group4 <- c(72.16,82.57,73.36,66.13,68.23) #S2
group5 <- c(86.29,89.77,88.83,86.85,88.50) #Baseline-S3
group6 <- c(56.76,65.65,61.98,63.78,59.04) #S3



# Calculate the Vargha-Delaney effect size for Baseline vs S1
print(paste("Effect size for Baseline vs S1:"))
VD.A(group1, group2)

# Calculate the Vargha-Delaney effect size for S1 vs Baseline
print(paste("Effect size for S1 vs Baseline:"))
VD.A(group2, group1)


# Calculate the Vargha-Delaney effect size for Baseline vs S2
print(paste("Effect size for Baseline vs S2:"))
VD.A(group3, group4)

# Calculate the Vargha-Delaney effect size for S2 vs Baseline
print(paste("Effect size for S2 vs Baseline:"))
VD.A(group4, group3)


# Calculate the Vargha-Delaney effect size for Baseline vs S3
print(paste("Effect size for Baseline vs S3:"))
VD.A(group5, group6)

# Calculate the Vargha-Delaney effect size for S3 vs Baseline
print(paste("Effect size for S3 vs Baseline:"))
VD.A(group6, group5)

