from tools.get_info import get_date, get_rate


def get_text():
    template = "Today, " + get_date() + " the Russian Ruble was " + str(get_rate()) + " USD"
    return template
