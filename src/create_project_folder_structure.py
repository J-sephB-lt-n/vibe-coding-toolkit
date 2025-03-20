
import argparse
import json
from pathlib import Path

from src.filepaths import filetree_string

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
        filepaths: list[Path] = [args.output_dir / Path(x) for x in json.load(file)]

    assert isinstance(filepaths, list)

    print("The following files and folders will be created:\n")
    print(filetree_string(filepaths))
    print()
    confirm: str = input("Please confirm creation (anything other than 'yes' will abort): ")
    if confirm != "yes":
        print("process aborted")
        exit()

    for path in filepaths:
        if path.suffix: # assume is a file
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
        else: # assume is a directory
            path.mkdir(parents=True, exist_ok=True)
    print("finished")
