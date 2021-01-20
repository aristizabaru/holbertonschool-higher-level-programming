#!/usr/bin/python3
"""module 7-add_item

Adds all arguments to a Python list, and then save them to a file:
"""
import json
import sys

# load functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
# config
file_name = "add_item.json"
# load json or create new list
try:
    json_object = load_from_json_file(file_name)
except Exception:
    json_object = list()
# read arguments from stdin
arguments = list()
for arg in sys.argv:
    arguments.append(arg)
del arguments[0]
# merge lists
json_object += arguments
save_to_json_file(json_object, file_name)
