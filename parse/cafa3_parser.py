#!/usr/bin/env Python3

import sys
import os

infile = open(sys.argv[1], "r")
outfile = open("uniprot_sprot_exp.csv", "w")

#outfile.write("Lable,Sequence" + "\n")

temp = ""
tempSeq = ""

for line in infile: #purpose of this loop is to get the start of each amino acid chain   
  if line.startswith(">"):
    if temp != "" and tempSeq != "":
      outfile.write(temp + tempSeq + "\n")
    temp = ""
    tempSeq = ""
    temp = line.strip("\n")
    temp = temp[1:]
    temp += ","
    continue
  
  tempSeq = tempSeq + line.strip("\n")
 
infile.close()
outfile.close()
