import datetime


def format_date(seconds: datetime.timedelta):
    names = ["year", "month", "day", "hour", "minute", "second"]

    formatted_date = convert_date(int(seconds.total_seconds()))

    if formatted_date[3] < 24 and formatted_date[2] < 1:
        return f"{seconds} elapsed"

    for time_ in formatted_date:
        if time_:
            return f"for {time_} {names[formatted_date.index(time_)]}{'s' if time_ > 1 else ''}"


def convert_date(seconds: int):
    """Converts a date into years, months, days, hours, minutes and seconds.
    """
    years, months = divmod(seconds, 3600 * 24 * 365)
    months, days = divmod(months, 3600 * 24 * 30)
    days, hours = divmod(days, 3600 * 24)
    hours, minutes = divmod(hours, 3600)
    minutes, seconds = divmod(minutes, 60)
    seconds, _ = divmod(seconds, 1)
    return years, months, days, hours, minutes, seconds
