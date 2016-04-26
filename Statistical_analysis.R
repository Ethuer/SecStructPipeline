#source("http://www.bioconductor.org/biocLite.R")
#biocLite("t.test")
#install.packages("UsingR")
#library(t.test)
#library(argparse)
#library(UsingR)

# packages for normal distribution
# install.packages("nortest")
# use lilliefors test for normal distribution on row_data
#library('nortest')


# usage    
#RScript InFile OutFile


args <- commandArgs(trailingOnly = TRUE)

# set working directory to current directory
# make it commandline driven
# workDir <- getwd()
# workDir


# Do a Upper Tail Test of Population Mean
# Explanation : http://www.r-tutor.com/elementary-statistics/hypothesis-testing/lower-tail-test-population-mean-unknown-variance

# correct with bonferroni-holm 

# argparse
#parser <- ArgumentParser(description=
#                           '
#Script takes parsed prediciton output of Minimal free energy, and tests if first column value is significantly lower than rest
#'
#)



hypotest <- function(row ){
  n <- 20
  alpha <- 0.05
  testsample <- row[1]
  row_data <- row[-1]
  mean_row <- mean(row_data)
  stdev <- sd(row_data, na.rm = FALSE)
  z = (mean_row - testsample)/(stdev/sqrt(n))
  #z.alpha = qnorm(1-alpha)
  #-z.alpha
  pval = pnorm(z)
  return(pval)
}

hypotest_up <- function(row ){
  n <- 20
  alpha <- 0.05
  testsample <- row[1]
  row_data <- row[-1]
  mean_row <- mean(row_data)
  stdev <- sd(row_data, na.rm = FALSE)
  t = (mean_row - testsample)/(stdev/sqrt(n))
  pval = pt(t, df=n-1, lower.tail=FALSE) 
  return(pval)
}

se <-  read.table(args[1], 
                  sep="\t", 
                  #col.names=c("id", "name"), 
                  header = FALSE,
                  fill=FALSE, 
                  strip.white=TRUE,
                  )

#head(se)
# test if the data is normally distributed via lillifors norm test
# http://www.inside-r.org/packages/cran/nortest/docs/lillie.test
#lillie.test(se)

# tested for replicates,  uncomment to redo, but not necessary for each run


#norm <- apply(se,1,lillie.test)
#sample <- se$V1


se <- as.matrix(se)
probabilities <- apply(se,1,hypotest_up)
# adjust against multiplicity
# bonferroni,  lets use holm
probabilities_adjusted <- p.adjust(probabilities, method ="holm", n = length(probabilities))
#tail(probabilities_adjusted)

write.csv(probabilities_adjusted,file=args[2])


#shuffle <- se[ , c(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)] 

#shuffleM <- as.matrix(shuffle)

#mean <- apply(se,1,mean)
#head(mean)
#head(shuffle)
#var <- apply(se,1,var)

#r_normalized <- apply(shuffleM,1,rnorm)

#x<-rnorm(10,0,5)
#ztest <- apply(se,1,simple.z.test(rnorm(se[ , c(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)] ),se$V1))

#??apply()

# standard error
#SE = s * sqrt{ ( 1/n ) * ( 1 - n/N ) * [ N / ( N - 1 ) ] } 

