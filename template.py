import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  # Setting up logging

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Creating a Path object for the file
    filedir, filename = os.path.split(filepath)  # Splitting the file path into directory and filename
    
    if filedir:  # Check if the directory is not empty
        if not os.path.exists(filedir):
            logging.info(f"Creating directory: {filedir}")
            os.makedirs(filedir, exist_ok=True)  # Creating the directory if it doesn't exist
            logging.info(f"Created directory: {filedir}")
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        logging.info(f"Creating file: {filepath}")
        with open(filepath, 'w') as file:
            file.write("")  # Creating the file if it doesn't exist
        logging.info(f"Created file: {filename}")
    else:
        logging.info(f"File already exists: {filename}")