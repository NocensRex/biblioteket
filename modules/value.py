# DONE: Base value
# All media types have 100% of purchase value att purchase year.
# Value falls with 10% every year

# DONE: Value of book
# An old book (age > 50 year) does not lose any more value, it increases with 8% every year instead.

# DONE: Value of music-cd
# Music-CD changes value depending on the amount of the same object (title and artist)
# purchase_price / amount rounded to closest krona

# DONE: Value of movie
# Value on movies is calculated based on degree of wear and the age of the movie (Base value)
# A wear value of 10 is mint condition and the value is 100% of purchase price.
# A wear value of 1 is very worn and the value is only 10% of purchase price.
# Base value * 0.X where X is wear value.

# FIXME: Round the final numbers to something easier for the eyes
import datetime


TODAY = datetime.datetime.today()


def current_value(purchase_price, age):
    'This will calculate the base value of an object'
    value = purchase_price
    if age != 0:
        for year in range(1, age+1):
            value = value * 0.9
    return value


def book_value(purchase_price, purchase_year):
    'This will recalculate the value of a book if it is older than 50 years'
    age = TODAY.year - purchase_year
    if age > 50:
        value = current_value(purchase_price, 50)
        for year in range(51, age+1):
            value = value * 1.08
    else:
        value = current_value(purchase_price, age)
    return round(value, 2)


def cd_value(purchase_price, amount):
    'This will calculate the price of a cd object based on the amount of similar cds'
    return int(round(purchase_price / amount))


def movie_value(purchase_price, purchase_year, degree_of_wear):
    'This will calculate the value of a movie based on the base value and degree of wear'
    age = TODAY.year - purchase_year
    value = current_value(purchase_price, age) * float(f'0.{degree_of_wear}')
    return round(value, 2)
