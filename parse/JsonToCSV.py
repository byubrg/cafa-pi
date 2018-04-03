import sys
import json

json_file = open("example_2.json")
json_str = json_file.read()
json_dict = json.loads(json_str)