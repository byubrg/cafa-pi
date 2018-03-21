#!/usr/bin/env bash

#download sequences and annotations
#wget http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_17_2/Pseudomonas/complete/gtf-complete.tar.gz
#download the amino acide sequences
wget http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_17_2/Pseudomonas/complete/faa-complete.tar.gz
#downlaod genes and intergenic annotations
#wget http://www.pseudomonas.com/downloads/pseudomonas/pgd_r_17_2/Pseudomonas/complete/gt-all-complete.tar.gz



#also available are gene annotations and gene and intergenic annotations

#unzip these files
#tar -xzf gtf-complete.tar.gz
tar -xzf faa-complete.tar.gz
#tar -xzf gt-all-complete.tar.gz 
