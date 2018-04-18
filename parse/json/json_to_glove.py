#! /usr/bin/env python
import sys
import json

infile = open(sys.argv[1], 'r')
json_dict = json.load(infile)

print ("here")
for line in infile:
    str_l = line
    json_dict = json.load(str_l)
print json_dict


GO:0030430