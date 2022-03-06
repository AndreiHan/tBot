import math
from datetime import date

from forex_python.converter import CurrencyRates


def get_rate():
    c = CurrencyRates()
    number = c.get_rate('RUB', 'USD')
    return truncate(number, 9)


def get_date():
    today = date.today()
    # Month abbreviation, day and year
    return today.strftime("%b-%d-%Y")


def truncate(number, decimals=0):
    if decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
