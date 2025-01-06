import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox containing the data.

    Args:
    path_to_yaml (Path): The path to the YAML file.

    Raises:
    ValueError: If the file is empty.
    e: empty file
    
    Returns:
    ConfigBox: A ConfigBox containing the data from the YAML file.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"yaml file: {path_to_yaml} is empty")
        raise ValueError("The yaml file is empty.")
    except Exception as e:
        logger.error(f"Error occurred while reading yaml file: {path_to_yaml}")
        raise e

@ensure_annotations
def create_directory(directory_paths: list, verbose = True):
    """
    Creates directories if they don't exist.

    Args:
    directory_paths (list): A list of directory paths to be created.
    verbose (bool): If True, prints the created directory paths.
    """
    for path in directory_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in bytes, kilobytes, megabytes, or gigabytes.
    
    Args:
    path (Path): The path to the file.

    Returns:
    str: The size of the file in bytes, kilobytes, megabytes, or gigabytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"