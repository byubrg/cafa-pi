#!/usr/bin/env python
import sys
import requests
import argparse


def RetrieveGOData(goid, readable):
	pre_query = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
	query_id = goid.replace(":", "%3A")
	full_query = pre_query + query_id + "/complete"

	r = requests.get(full_query, headers = {"Accept" : "application/json"})
	if not r.ok:
		r.raise_for_status()
		sys.exit()

	if readable:
		import json
		parsed_json = json.loads(r.text)
		id = args.go_id
		name =  parsed_json["results"][0]["name"]
		definition = parsed_json["results"][0]["definition"]["text"]
		outfile.write("GO ID:\n" ,'\t', id)
		#print ("GO ID:\n" ,'\t', id)
		outfile.write("Name:\n", '\t', name)
		#print ("Name:\n", '\t', name)
		outfile.write("Definition:\n", '\t', definition)
		#print ("Definition:\n", '\t', definition)
		try:
			synonyms = parsed_json["results"][0]["synonyms"]
		except:
			synonyms = None
		if synonyms:
			outfile.write("Synonyms:")
			#print ("Synonyms:")
			for e in synonyms:
				outfile.write('\t', e["name"])
			#	print ('\t', e["name"])
			
		#should be parsed_json["results"][0]["name"]
	else:
		outfile.write(r.text)
		#print(r.text)


if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument("go_id", nargs='*', help = "Enter the GO_ID(s) you would like to lookup. A list of space-separated terms is also acceptable")
	p.add_argument("-f", "--go_id_file", help = "A file containing a list of newline separated GO_terms to look up")
	p.add_argument("-r", "--human_readable", action = "store_true", help = "Specify if you would like stuff printed in user friendly fashion")
	args = p.parse_args()

	if len(args.go_id) == 0 and args.go_id_file == None:
		print ("Please specify either valid GO term(s) or a file listing GO terms")
		print ("Program will terminate")
		sys.exit()
	
	if args.go_id:
		for goid in args.go_id:
			RetrieveGOData(goid, args.human_readable)
			print()
	if args.go_id_file:
		outfile = open("json_data.txt", 'w')
		counter = 0
		with open(args.go_id_file, "r") as go_in:
			for line in go_in:
				counter+=1
				if counter == 101:
					break
				print("Line: "+str(counter))
				if "GO" in line:
					RetrieveGOData(line.strip(), args.human_readable)
					outfile.write('\n')
					#print()
				else:
					print("File in has invalid terms. Please try again")
					sys.exit()
				
		go_in.close()
		outfile.close()