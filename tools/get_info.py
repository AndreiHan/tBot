from datetime import date

from forex_python.converter import CurrencyRates


def get_rate():
    c = CurrencyRates()
    return c.get_rate('RUB', 'USD')


def get_date():
    today = date.today()
    # Month abbreviation, day and year
    return today.strftime("%b-%d-%Y")
