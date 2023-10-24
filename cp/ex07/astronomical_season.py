"""Exercise 7.9: Astronomical season."""

month_name_to_month_number = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def astronomical_season(date :  tuple) -> str:
    """Return the astronomical season of the given date.

    :param date: Tuple with the given date.
    :return: String with astronomical season
    """
    month = month_name_to_month_number[date[1]]
    day = date[0]
    rel = day+100*month
    if rel >= 320 and rel < 621:
        season = 'spring'
    elif rel >= 621 and rel < 923:
        season = 'summer'
    elif rel >= 923 and rel < 1221:
        season = 'autumn'
    else:
        season = 'winter'
    return season
