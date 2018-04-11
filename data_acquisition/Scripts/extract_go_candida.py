#!/usr/bin/env python3
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
import argparse
import re
import subprocess

def OutputRelevant(id, trans, go):
	ps = id + "," + trans + ","
	if not go:
		return
	for g in go:
		ps = ps + g + ","
	print(ps[0:-1])


def LookupGo(name):
	path = '/fslhome/aromdahl/fsl_groups/fslg_BRG2/cafa-pi/cafa-pi/data_acquisition/candida_annots.cgd'
	try:
		ret = subprocess.Popen(["grep", name, path], stdout = subprocess.PIPE)
		out_two = subprocess.check_output(["cut", "-f", "5"], stdin = ret.stdout)
		#print(out_two)
		go_terms = str(out_two.strip()).replace("\'","")
		#print(go_terms)
		go_terms = go_terms[1:].split('\\n')
		#print (set(go_terms))
		#input()
		return set(go_terms)
	except subprocess.CalledProcessError:
		print ("error")
	
def ManualParse(fp):
	fasta_sequences = SeqIO.parse(open(fp),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		go_terms = LookupGo(name)
		OutputRelevant(name, sequence, go_terms)


if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument("gbk_dir", help = "Directory containing fa files")
	args = p.parse_args()

	for gbk in os.listdir(args.gbk_dir):
		if ".fa" in gbk:
			f_p = args.gbk_dir + "/" + gbk
			print (f_p)
			ManualParse(f_p)	


			"""try:
				p_gbk = [rec for rec in SeqIO.parse(f_p, "genbank")]
			except AssertionError:
				print "error"
				continue
			print (len(p_gbk))
			input()
			"""
			



