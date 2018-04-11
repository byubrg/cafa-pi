#############
#INPUT: txt file with json files on each line
#OUTPUT: tsv- each line corresponds to a json but only contains:
# 1 name
# 2 definition 
# 3 synonyms if they exist



import sys
import json
import csv 

#################
#######CONVERT NECESSARY DATA INTO A LIST 
#################3
#want name, definition, text and synonym (no synonym in this example)
def CreateOutputList(json_dict):
	outputList = []
	mini_dict = json_dict['results'][0]
	outputList.append(mini_dict['name'])
	outputList.append(mini_dict['definition']['text'])
	synonym = mini_dict.get('synonyms', "NULL")
	if synonym != "NULL":
    		outputList.append(mini_dict['synonyms'][0]['name'])
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
#################3
json_file = open("json_data.txt")
json_str = json_file.readline()
ofstream = open("GOIdInfo.csv", 'w')
while json_str:
	json_dict = json.loads(json_str)
	outputList = CreateOutputList(json_dict)
	ListToCsv(outputList, ofstream)
	json_str = json_file.readline()
ofstream.close()
of = open("GOIdInfo.csv", 'r')
mystr = of.read()
print(mystr)
ofstream.close()
json_file.close()
