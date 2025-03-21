import argparse
import json
from pathlib import Path

from src.prompts import prompts_env

prompt_template = """
Please write me the content for the following files:

{% for filepath in filepaths %}
- {{ filepath }}
{% endfor %}

For each file, output the file path followed immediately by a markdown codeblock \
containing the file contents, for example:
<file-output-example>
/app/app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Working!"
```
</file-output-example>

Write high quality production code - as would be found in a modern enterprise \
codebase.
"""

prompt = prompts_env.from_string(prompt_template)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i",
        "--input_filepaths_list",
        type=Path,
        required=True,
        help="Path to .json file containing paths of files to populate",
    )
    args = arg_parser.parse_args()

    with open(args.input_filepaths_list, "r") as file:
        filepaths: list[Path] = [Path(filepath) for filepath in json.load(file)]

    print(
        prompt.render(
            filepaths=filepaths,
        ),
    )
