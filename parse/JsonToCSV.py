import sys
import json
import csv 

#################
#######CONVERT JSON TO DICT
#################3
json_file = open("proteinData.json")
json_str = json_file.read()
json_dict = json.loads(json_str)
json_file.close()

#################
#######CONVERT NECESSARY DATA INTO A LIST 
#################3
#want name, definition, text and synonym (no synonym in this example)
outputList = []
outputList.append(json_dict['results'][0]['name'])
outputList.append(json_dict['results'][0]['definition']['text'])

#############
#######APPEND OUTPUT TO CSV
#############
with open("GOIdInfo.csv", 'ab') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #wr.writerow([str(d, 'UTF-8') for d in outputList])
    #wr.writerow(outputList)
    #wr.writerow(bytes(outputList, 'UTF-8'))
    print(outputList)
