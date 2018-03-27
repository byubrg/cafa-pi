#!/usr/bin/env bash

#download the annotations
wget http://www.candidagenome.org/download/go/gene_association.cgd.gz


#also available are gene annotations and gene and intergenic annotations

#unzip these files
gunzip gene_association.cgd.gz
