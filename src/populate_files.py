"""
Functions for writing file contents
"""

import argparse
from collections import namedtuple
from pathlib import Path
import re

from src import config
from src.filepaths import filetree_string


def populate_file_contents(llm_generated_file_contents: str):
    find_markdown_blocks = re.findall(
        r"(\S*\/\S*)\s*\n```(\w+)\s*\n(.*?)\n```",
        llm_generated_file_contents,
        re.DOTALL,
    )
    if not find_markdown_blocks:
        print("WARNING: Did not find any markdown code blocks")
        exit()

    FileContents = namedtuple("FileContents", ["filepath", "language", "file_contents"])

    file_contents: list[FileContents] = []
    for markdown_block in find_markdown_blocks:
        if len(markdown_block) != 3:
            print(
                "WARNING: encountered markdown block with unexpected number of elements.",
                "\n\tExpected number of elements is 3: (filepath, language, file_content)"
                "\n\tHere is the extracted content:\n",
                markdown_block,
            )
            continue
        file_contents.append(
            FileContents(
                filepath=Path(markdown_block[0]),
                language=markdown_block[1].strip(),
                file_contents=markdown_block[2],
            )
        )

    filepaths_to_be_edited: list[tuple[Path, FileContents]] = []
    for file_content in file_contents:
        filepath_to_edit: Path = (
            config.LLM_CODE_APP_ROOT_DIR
            / file_content.filepath.relative_to(file_content.filepath.anchor)
        )
        if not filepath_to_edit.exists():
            print(
                "WARNING: LLM has generated code for a file which does not exist: ",
                f"\n\t'{filepath_to_edit}'" "\n\t(skipping this file)",
            )
        else:
            filepaths_to_be_edited.append(
                (
                    filepath_to_edit,
                    file_content,
                )
            )

    if len(filepaths_to_be_edited) == 0:
        print("WARNING: No files to write - exiting")
        exit()

    print("PLEASE CONFIRM: The contents of the following files will be overwritten:")
    print(filetree_string([x[0] for x in filepaths_to_be_edited]))
    user_confirm: str = input(
        "Confirm file writing/overwriting (anything other than 'yes' will abort): ",
    )
    if user_confirm != "yes":
        print("script exited")
        exit()

    for filepath, file_content in filepaths_to_be_edited:
        print(f"writing to file {filepath}", end="")
        with open(filepath, "w") as file:
            file.write(file_content.file_contents)
        print("...done")

    print("finished")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i",
        "--input_file_contents",
        required=True,
        type=Path,
        help="Path of markdown file containing all LLM-generated app code",
    )
    args = arg_parser.parse_args()

    with open(args.input_file_contents, "r") as file:
        llm_generated_file_contents: str = file.read()

    populate_file_contents(llm_generated_file_contents)
