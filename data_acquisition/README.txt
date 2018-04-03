Important documents in this directory:
	
Fields selected (in this order):
Acc (id)
Gene/product (bioentity)
Gene/roduct (bioentity_label)
Direct annotation (annotation_class_list)
Direct annotation (annotation_class_list_label)
Organism (taxon_label)
Organism (taxon_subset_closure_label)
Synonyms
Type
	bacteria_biofilm_annotation:
		212 proteins from GO that have the biofilm annotation
(GO:0042710) and are found in bacteria
	bacteria_motility_annotation.txt:
		675 proteins from GO that have the motility Go annotation
(GO:GO:0001539) and are found in bacteria



Pseudomonas_proteins	
This directory contains 215 .faa files listing proteins for 215 strains of
Pseudomonas. Data was taken from http://www.pseudomonas.com/strain/download,
see the download script in the Scripts folder for exact download procedure.
	-This totals to 41 known unique species and 22 unknown species (for a
	total of 63 species, 215 different strains
	-This dataset contains 1195496 proteins, 300926 (roughly 25%) of which
	are labelled as "hypothetical proteins"
	-As a result, there is a high level of redundancy in protein sequences
	here, since many of these files are sequences from varying strains in
	the same species.
	-Of these proteins, 728 are involved in biofilm synthesis, formation,
	or dispersion
Pseudomonas_annots
	This directory contains all the annotations for each of these files.
Note that GO annotions vary from strain to strain; however, there are 1199243
GO annotations total in the dataset

Candida_albicans
This directory contains 13 different fa files
	- This totals to 70291 different proteins we can use from 11 unique
	  organisms. 2 are substrains

 candida_annots.cgd	
This file contains the annots for all the proteins here, with 298270
total GO annotations
