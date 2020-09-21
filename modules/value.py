# TODO: Base value
# All media types have 100% of purchase value att purchase year.
# Value falls with 10% every year

# TODO: Value of book
# An old book (age > 50 year) does not lose any more value, it increases with 8% every year instead.

# TODO: Value of music-cd
# Music-CD changes value depending on the amount of the same object (title and artist)
# purchase_price / amount rounded to closest krona

# TODO: Value of movie
# Value on movies is calculated based on degree of wear and the age of the movie (Base value)
# A wear value of 10 is mint condition and the value is 100% of purchase price.
# A wear value of 1 is very worn and the value is only 10% of purchase price.
# Base value * 0.X where X is wear value.
import datetime


TODAY = datetime.datetime.today()


def current_value(purchase_price, age):
    value = purchase_price
    if age != 0:
        for year in range(1, age):
            value = value * 0.9
    return value


def book_value(purchase_price, purchase_year):
    age = TODAY.year - purchase_year
    if age > 50:
        value = current_value(purchase_price, 50)
        for year in range(51, age):
            value = value * 1.08
    else:
        value = current_value(purchase_price, age)
    return value


def cd_value(purchase_price, amount):
    return int(round(purchase_price / amount))


def movie_value(purchase_price, purchase_year, degree_of_wear):
    age = TODAY.year - purchase_year
    value = current_value(purchase_price, age) * float(f'0.{degree_of_wear}')
    return value
