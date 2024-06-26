from loguru import logger
from typing import Any
import os 
import json

def ensure_weights_file(zangief_dir_name, weights_file_name):
    if not os.path.exists(zangief_dir_name):
        os.makedirs(zangief_dir_name)
        logger.info(f"Created directory: {zangief_dir_name}")

    if not os.path.exists(weights_file_name):
        with open(weights_file_name, 'w') as file:
            json.dump({}, file)
        logger.info(f"Created file: {weights_file_name}")


def write_weight_file(weights_file, modules_info: dict[int, dict[str, Any]]):
    """
    Writes the modules and their scores to the weights.json file. Each module
    entry will contain the UID, SS58 address, and score.

    Args:
        modules_info: A dictionary mapping module UIDs to their addresses and score.
    """

    # Write the JSON structure to the file
    with open(weights_file, 'w') as file:
        json.dump(modules_info, file, indent=4)

def read_weight_file(weights_file):
    """
    Reads the modules and their scores from the weights.json file. 

    Returns:
        A dictionary mapping module UIDs to their addresses and score.
    """
    if not os.path.exists(weights_file):
        return {}

    with open(weights_file, 'r') as file:
        data = json.load(file)

    return data