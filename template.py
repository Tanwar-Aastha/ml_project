# Will create the structure of the project
# Creating files and folders automatically

import os
from pathlib import Path
import logging

# definging the projct name
while True:
    project_name = input('Enter a project name: ')
    if project_name != "":
        break

# list of required project files
project_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/logger.py",
    f"{project_name}/exception.py",
    f"{project_name}/utils.py",
    f"config/config.yaml",
    f"schema.yaml",
    f"setup.py",
    f"app.py"
]

for filepth in project_files:
    # converting the strings in the list into paths
    file_path = Path(filepth)

    # splitting the file and directory from the file_path formed
    file_dir, file_name = os.path.split(file_path)

    # checking if the file directory is correct or empty
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True) 

    # Creating the files
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as file:
            pass
    else:
        logging.info(f"These files already exists at {file_path}.")

