#!/usr/bin/python3
""" Load, add, save  """
from sys import argv
from typing import List
from os.path import exists

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_arguments_to_list(arguments: List[str]) -> None:

    """Add all arguments to a Python list and save them to a file."""

    try:
        if exists('add_item.json'):
            add_i = load_from_json_file('add_item.json')
            save_to_json_file(add_i + arguments, 'add_item.json')
        else:
            save_to_json_file(arguments, 'add_item.json')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_arguments_to_list(argv[1:])
