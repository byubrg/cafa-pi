#!/usr/bin/env python3
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
import argparse
import re

def OutputRelevant(id, trans, go):
	ps = id + "," + trans + ","
	for g in go:
		ps = ps + g + ","
	print(ps[0:-1])

def ManualParse(fp):
	with open(fp, 'r') as fstream:
		iter = 0
		saving = False
		translating = False
		translation = ""
		curr_gene = ""
		go_ids = []
		try:
			for line in fstream:
				if "gene" in line:
					saving = True
					iter += 1
					if iter > 1:
						OutputRelevant(curr_gene, translation, go_ids)
						translating = False
						translation = ""
						curr_gene = ""
						go_ids = []
				if saving:
					if "locus_tag" in line:
						get = re.search("\"(.*)\"", line.strip())
						curr_gene = get.group(1)
					if "translation" in line:
						translating = True
				if translating:
					get = re.search("[A-Z]+",line.strip())
					try:
						translation += get.group(0)
					except:
						translating = False
							
				if "GO:00" in line.strip():
					get = re.search("GO:[0-9]+", line.strip())
					go_ids.append(get.group(0)) 
		except UnicodeDecodeError:
			print ("error with", fp)
			return 				


if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument("gbk_dir", help = "Directory containing GBK files")
	args = p.parse_args()

	for gbk in os.listdir(args.gbk_dir):
		if ".gbk" in gbk:
			f_p = args.gbk_dir + "/" + gbk
			
			ManualParse(f_p)	


			"""try:
				p_gbk = [rec for rec in SeqIO.parse(f_p, "genbank")]
			except AssertionError:
				print "error"
				continue
			print (len(p_gbk))
			input()
			"""
			



