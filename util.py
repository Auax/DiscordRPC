# Util File

import json
import color

col = color.Color()


def logger(identifier, value, mode="normal") -> str:
    """
    Simple class to print logs
    :param identifier: Identifier KEY
    :param value: Value assigned to identifier KEY
    :param mode: Specify whether the message is an "error", a "success" or "normal"
    :return: str
    """

    assert mode == "normal" or "success" or "error", 'Mode must be "error", "success" or "normal".'

    if mode.lower() == 'normal':
        d = f"[{col.fore_color('^', 'YELLOW')}] {identifier}: {value}"

    elif mode.lower() == 'error':
        d = f"[{col.fore_color('!', 'RED')}] {col.fore_color(str(identifier), 'RED')}: {col.fore_color(str(value), 'RED')}"

    elif mode.lower() == 'success':
        d = f"[{col.fore_color('$', 'GREEN')}] {identifier}: {col.fore_color(str(value), 'GREEN')}"

    print(d)
    return d


def load_json(path: str) -> dict:
    """
    Read and return a JSON file.
    :param path: Path to config.json file
    :return: dict
    """
    with open(path) as file:
        data = json.load(file)

    return data
