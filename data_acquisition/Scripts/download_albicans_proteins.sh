#!/usr/bin/env bash

#download the amino acide sequences
wget http://www.candidagenome.org/download/sequence/C_albicans_SC5314/Assembly22/current/C_albicans_SC5314_A22_current_default_protein.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_albicans_WO-1/current/C_albicans_WO-1_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_dubliniensis_CD36/current/C_dubliniensis_CD36_current_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_glabrata_CBS138/current/C_glabrata_CBS138_current_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_guilliermondii_ATCC_6260/current/C_guilliermondii_ATCC_6260_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_lusitaniae_ATCC_42720/current/C_lusitaniae_ATCC_42720_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_lusitaniae_CBS6936/current/C_lusitaniae_CBS6936_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_orthopsilosis_Co_90-125/current/C_orthopsilosis_Co_90-125_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_parapsilosis_CDC317/current/C_parapsilosis_CDC317_current_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/C_tropicalis_MYA-3404/current/C_tropicalis_MYA-3404_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/D_hansenii_CBS767/current/D_hansenii_CBS767_orf_trans_all.fasta.gz
wget http://www.candidagenome.org/download/sequence/L_elongisporus_NRLL_YB-4239/current/L_elongisporus_NRLL_YB-4239_orf_trans_all.fasta.gz

#also available are gene annotations and gene and intergenic annotations

#unzip these files
gunzip C_albicans_SC5314_A22_current_default_protein.fasta.gz
gunzip C_albicans_WO-1_orf_trans_all.fasta.gz
gunzip C_dubliniensis_CD36_current_orf_trans_all.fasta.gz
gunzip C_glabrata_CBS138_current_orf_trans_all.fasta.gz
gunzip C_guilliermondii_ATCC_6260_orf_trans_all.fasta.gz
gunzip C_lusitaniae_ATCC_42720_orf_trans_all.fasta.gz
gunzip C_lusitaniae_CBS6936_orf_trans_all.fasta.gz
gunzip C_orthopsilosis_Co_90-125_orf_trans_all.fasta.gz
gunzip C_parapsilosis_CDC317_current_orf_trans_all.fasta.gz
gunzip C_tropicalis_MYA-3404_orf_trans_all.fasta.gz
gunzip D_hansenii_CBS767_orf_trans_all.fasta.gz
gunzip L_elongisporus_NRLL_YB-4239_orf_trans_all.fasta.gz

mv C_albicans_SC5314_A22_current_default_protein.fasta C_albicans_SC5314_A22_unknowns.fasta

