# vibe-coding-toolkit
Some convenience functions for facilitating vibe coding using just a chatbot (i.e. without requiring an AI-integrated IDE).

I really don't enjoy "vibe coding" at all. I feel that it makes me into a weaker developer and I find myself spending the entire development time debugging.

However, I do find the almost instant creation of throw-away POC web apps very powerful, which is why I wrote the scripts in this repo - they just do simple things like string templating, and creating and populating files and folders.

## Example workflow

Here is an example of how I used these scripts to make a very basic single page virus simulation web app:

1. First, I made a copy of my basic software requirements document template [templates/software_requirements_spec.md](./templates/software_requirements_spec.md) and saved it to [local_temp/software_requirements_spec.md](./local_temp/software_requirements_spec.md). Then I filled in the copy with my app requirements.

2. Then I ran this script, pointing it to my filled in requirements doc:

```bash
uv run python -m src.prompts.create_project_folder_structure \
  --requirements_doc 'local_temp/software_requirements_spec.md'
```

This script prints out a prompt to the terminal, which I then copied from my terminal and pasted into the ChatGPT web app. Once ChatGPT returned a folder structure to me, I removed some of the files which I didn't want and pasted the edited result into [local_temp/project_folder_structure.json](./local_temp/project_folder_structure.json).

3. I then ran this script to create the folder structure:

```bash
uv run python -m src.create_project_folder_structure \
  --input_filepaths_list 'local_temp/project_folder_structure.json' \
```

4. Then, I put a list of file paths which I wanted ChatGPT to write file contents for in [local_temp/filepaths_to_populate.json](./local_temp/filepaths_to_populate.json) and ran this script:

```bash
uv run python -m src.prompts.populate_files \
  --input_filepaths_list 'local_temp/filepaths_to_populate.json'
```

...which prints out a prompt to the terminal. I copied this prompt from my terminal and pasted it into the ChatGPT web app.

5. I copied the response from ChatGPT (containing the generated contents for my files) into [local_temp/files_contents.md](./local_temp/files_contents.md)

6. Then I ran this script, which populates my local files:
```bash
uv run python -m src.populate_files \
  --input_file_contents 'local_temp/files_contents.md'
```

Then I ran the app, and none of the buttons worked (typical finish haha). I told ChatGPT, and it corrected it's own error very easily. The app is not EXACTLY what I asked for, but it works fine. You can go try it by opening [local_temp/llm_app/virus-simulation-app/index.html](./local_temp/llm_app/virus-simulation-app/index.html)

