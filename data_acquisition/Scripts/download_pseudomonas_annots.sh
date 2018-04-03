#!/usr/bin/env bash

#download the annotations
wget http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_17_2/Pseudomonas/complete/gbk-complete.tar.gz



#also available are gene annotations and gene and intergenic annotations

#unzip these files
tar -xzf gbk-complete.tar.gz
mv gbk-complete psuedomonas_annots.gbk 
