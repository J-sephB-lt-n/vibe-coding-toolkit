# vibe-coding-toolkit
Some useful functions for facilitating vibe coding (without requiring an AI-integrated IDE).

I really don't enjoy "vibe coding" at all. I feel that it makes me into a weaker developer and I find myself spending the entire development time debugging.

However, I do find the one-time creation of POC web apps very powerful, and I'm including my utility scripts for this specific application in this repo.

## Example workflow

1. Make a copy of [templates/software_requirements_spec.md](./templates/software_requirements_spec.md), saving it to [local_temp/software_requirements_spec.md](./local_temp/software_requirements_spec.md), and fill it in.

2. 

```bash
uv run python -m src.prompts.create_project_folder_structure \
  --requirements_doc 'local_temp/software_requirements_spec.md'
```

I dumped the JSON list of filepaths to create in [local_temp/project_folder_structure.json](./local_temp/project_folder_structure.json)


```bash
uv run python -m src.create_project_folder_structure \
  --input_filepaths_list 'local_temp/project_folder_structure.json' \
  --output_dir 'local_temp'
```
