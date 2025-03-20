
import argparse
import json
from collections import defaultdict
from pathlib import Path

def build_filetree(paths: list[Path]) -> defaultdict:
    tree = defaultdict(dict)
    
    for path in paths:
        parts = path.parts
        node = tree
        for part in parts[:-1]:  # Traverse directories
            node = node.setdefault(part, {})
        node[parts[-1]] = None  # Mark file nodes with None
    
    return tree

def print_tree(node, prefix=""):
    for key, sub_node in sorted(node.items()):
        print(prefix + "├── " + key)
        if isinstance(sub_node, dict):
            print_tree(sub_node, prefix + "│   ")

if __name__ == "__main__":
    arg_parser=argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i", 
        "--input_filepaths_list",
        help="path to .json file containing filepaths to create",
        type=Path,
    )
    arg_parser.add_argument(
        "-o",
        "--output_dir",
        help="directory in which to create the new files and folders", 
        type=Path,
    )
    args = arg_parser.parse_args()

    with open(args.input_filepaths_list, "r") as file:
        filepaths: list[Path] = [Path(x) for x in json.load(file)]

    assert isinstance(filepaths, list)

    print("The following files and folders will be created:\n")
    file_tree = build_filetree(filepaths)
    print_tree(file_tree)
    print()
    confirm: bool = input("Please confirm creation (anything other than 'yes' will abort): ") == "yes"
    if confirm != "yes":
        exit()
