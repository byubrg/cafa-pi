#!/usr/bin/env python
import sys
import requests
import argparse


p = argparse.ArgumentParser()
p.add_argument("go_id", help = "Enter the GO_ID you would like to lookup")
p.add_argument("-r", "--human_readable", action = "store_true", help = "Specify if you would like stuff printed in user friendly fashion")
args = p.parse_args()

pre_query = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
query_id = args.go_id.replace(":", "%3A")
full_query = pre_query + query_id + "/complete"

r = requests.get(full_query, headers = {"Accept" : "application/json"})
if not r.ok:
	r.raise_for_status()
	sys.exit()

if args.human_readable:
	import json
	parsed_json = json.loads(r.text)
	id = args.go_id
	name =  parsed_json["results"][0]["name"]
	definition = parsed_json["results"][0]["definition"]["text"]
	print "GO ID:\n" ,'\t', id
	print "Name:\n", '\t', name
	print "Definition:\n", '\t', definition
	try:
		synonyms = parsed_json["results"][0]["synonyms"]
	except:
		synonyms = None
	if synonyms:
		print "Synonyms:"
		for e in synonyms:
			print '\t', e["name"]
		
	#should be parsed_json["results"][0]["name"]
else:
	print(r.text)