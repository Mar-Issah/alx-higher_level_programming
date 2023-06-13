#!/usr/bin/python3
"""Imported module for add_item"""
import sys
import json
import os.path


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


json = "add_item.json"
arr = []

if os.path.exists(json):
    arr = load_from_json_file(json)

for arg in range(1, len(sys.argv)):
    arr.append(sys.argv[arg])

save_to_json_file(arr, json)
