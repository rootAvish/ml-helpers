import logging


def json_loader(json_file_path):
    """Read a JSON from file and return it, in unicode if on Python3.

    :param json_file_path: The path to the json file.
    """
    logger = logging.getLogger("json_loader")
    try:
        with open(json_file_path, 'r') as file_stream:
            import json
            return json.load(file_stream)
    except FileNotFoundError:
        logger.error("No such file exists, cannot return a json.")
