#############
#INPUT: txt file with json files on each line
#OUTPUT: tsv- each line corresponds to a json but only contains:
# 1 name
# 2 definition 
# 3 synonyms if they exist


import re
import sys
import json
import csv 

#################
#######CONVERT NECESSARY DATA INTO A LIST 
#################3
#want name, definition, text and synonym (no synonym in this example)
def CreateOutputList(json_dict):
	outputList = []
	#mini_dict = json_dict['results'][0]
	outputList.append(json_dict['name'])
	outputList.append(json_dict['definition']['text'])
	synonym = json_dict.get('synonyms', "NULL")
	if synonym != "NULL":
    		outputList.append(json_dict['synonyms'][0]['name'])
	return outputList

#############
#######APPEND OUTPUT TO TSV
#############
def ListToCsv( myList, ofstream ):
	firstVar = True
	for item in outputList:
		if(firstVar):
			ofstream.write(item)
			firstVar = False
		else:
			ofstream.write('\t' + item)	
	ofstream.write('\n')

#################
#######CONVERT JSON TO DICT
##################
json_file = open("json_of_unique_ids.txt")
json_str = json_file.readline()
ofstream = open("GOIdInfo.tsv", 'w')
i = 0
while json_str:
	#r = re.search(r'{"id":.*"usage".*}', json_str)
	r = re.search(r'{"id":.*"usage"(.){0,20}}', json_str)
	json_str = r.group(0)
	json_dict = json.loads(json_str)
	outputList = CreateOutputList(json_dict)
	ListToCsv(outputList, ofstream)
	json_str = json_file.readline()
	i += 1
	#print(i)
ofstream.close()
ofstream.close()
json_file.close()

