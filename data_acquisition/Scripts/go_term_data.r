#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
#args[1] is the GO term

#Make sure the package is installed
GOPkgTest <- function()
{
  if (!require('GO.db',character.only = TRUE))
  {
    source("https://bioconductor.org/biocLite.R")
    biocLite("GO.db")
    if(!require('GO.db',character.only = TRUE)) stop("Package not found")
  }
}

print(args[1])
invisible(library('GO.db'))
GOTERM$args[1]

