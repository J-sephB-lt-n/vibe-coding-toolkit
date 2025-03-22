import argparse
from pathlib import Path

from src.prompts import prompts_env

prompt_template = """
You are a lead developer on a software application.

Here are the application requirements:

{{ software_requirements_spec }}

Please ask me clarifying questions if any part of this requirements spec is unclear.
"""

prompt = prompts_env.from_string(prompt_template)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-r",
        "--requirements_doc",
        type=Path,
        required=True,
    )
    args = arg_parser.parse_args()
    with open(args.requirements_doc, "r") as file:
        requirements_spec: str = file.read()
    print(
        prompt.render(
            software_requirements_spec=requirements_spec,
        ),
    )
