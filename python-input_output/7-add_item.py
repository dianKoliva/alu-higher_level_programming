#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
from typing import List
from os.path import exists
from json import dump, load


def save_to_json_file(my_obj: List, filename: str):
    """ Saves an object to a JSON file """
    with open(filename, mode='w', encoding='utf-8') as f:
        dump(my_obj, f)


def load_from_json_file(filename: str) -> List:
    """ Loads an object from a JSON file """
    if exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            return load(f)
    return []


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
