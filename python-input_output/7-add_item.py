#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves to JSON file."""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Yoxla fayl mövcuddurmu
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Bütün command line argument-ləri əlavə et
my_list.extend(sys.argv[1:])

# JSON fayla yaz
save_to_json_file(my_list, filename)
