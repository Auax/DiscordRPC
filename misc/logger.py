from misc import color

col = color.Color()


def logger(identifier, value, mode="info") -> str:
    """
    Simple class to print logs
    :param identifier: Identifier KEY
    :param value: Value assigned to identifier KEY
    :param mode: Specify whether the message is an "error", a "success" or "normal"
    :return: str
    """

    assert mode in ["info", "success", "error"], 'Mode must be "error", "success" or "normal".'

    if mode.lower() == 'info':
        log = f"[{col.fore_color('^', 'YELLOW')}] {identifier}: {value}"

    elif mode.lower() == 'error':
        log = f"[{col.fore_color('!', 'RED')}] {col.fore_color(str(identifier), 'RED')}: " \
              f"{col.fore_color(str(value), 'RED')}"

    elif mode.lower() == 'success':
        log = f"[{col.fore_color('$', 'GREEN')}] {identifier}: {col.fore_color(str(value), 'GREEN')}"

    print(log)
    return log
