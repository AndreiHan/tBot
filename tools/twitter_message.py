from datetime import date


def get_date():

    today = date.today()

    # Month abbreviation, day and year
    d4 = today.strftime("%b-%d-%Y")
    print("d4 =", d4)