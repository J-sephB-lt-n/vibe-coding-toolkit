import argparse
from pathlib import Path

from src.prompts import prompts_env

prompt_template = """
You are a lead developer on a software application.

Here are the application requirements:

{{ software_requirements_spec }}

Please propose a project folder structure for this software application (directories \
and files), as would be found in a high quality modern enterprise codebase.

Please include a file tree diagram in your response, as well as a matching list of paths as \
a valid JSON list of unix paths (refer to output format example below):

<example-paths-list>
```json
[
    "app/app.py",
    "app/requirements.txt",
    "app/templates/index.html",
    "app/static/style.css",
    "app/static/script.js",
    "app/static/logo.png"
]
```
</example-paths-list>
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
