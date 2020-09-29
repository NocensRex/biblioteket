import datetime

from modules.utils import str_sized


class Lib:
    def __init__(self):
        self.media = []

    def update_prices(self):
        for elm in self.media:
            if elm.NEED_DUPLICATES_AMOUNT:
                elm.update_current_price(self.find_duplicates(elm))
            else:
                elm.update_current_price()

    def find_duplicates(self, item):
        count = 0
        for elm in self.media:
            if item.NEED_DUPLICATES_AMOUNT:
                if elm.title == item.title and elm.creator == item.creator:
                    count += 1
            else:
                count = None
        return count


class Media:
    subclasses = {}

    def __init__(self, title, creator, purchase_price, purchase_year=None):
        self.mediatype = self.__class__.__name__
        self.title = title
        self.creator = creator
        self.purchase_price = float(purchase_price)
        self.current_price = float(purchase_price)
        if purchase_year is not None:
            self.purchase_year = int(purchase_year)
            self.age = datetime.datetime.today().year - self.purchase_year

    def base_price(self, age=None) -> float:
        'This will calculate the base value of an object'
        if age is not None:
            temp_age = age
        else:
            temp_age = self.age
        value = self.purchase_price
        if temp_age != 0:
            for year in range(1, temp_age+1):
                value = value * 0.9
        return value

    @classmethod
    def register_subclass(cls, media_type):
        def decorator(subclass):
            cls.subclasses[media_type] = subclass
            return subclass
        return decorator

    @classmethod
    def create(cls, mediatype, params):
        if mediatype not in cls.subclasses:
            raise ValueError(f'{mediatype} is not a an acceptable mediatype')

        return cls.subclasses[mediatype](*params)

    def __repr__(self):
        if self.purchase_year is not None:
            return f'{self.__class__.__name__}({self.title}{self.creator}{self.purchase_price}{self.current_price}{self.purchase_year}{self.age}'
        else:
            return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}'


@Media.register_subclass('book')
class Book(Media):
    mediatype = 'book'
    NEED_DUPLICATES_AMOUNT = False

    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        super().__init__(title, author, purchase_price, purchase_year)
        self.page_count = int(page_count)

    def update_current_price(self):
        'This will recalculate the value of a book if it is older than 50 years'
        price = self.purchase_price
        if self.age > 50:
            price = super().base_price(50)
            for year in range(51, self.age+1):
                price = price * 1.08
                self.current_price = round(price, 2)
        else:
            price = super().base_price()
            self.current_price = round(price, 2)

    def save(self) -> list:
        return Book.mediatype, self.title, self.creator, self.page_count, self.purchase_price, self.purchase_year

    def __str__(self):
        return (''
                + str_sized(self.title, 29).ljust(30)
                + str_sized(self.creator, 29).rjust(30)
                + str_sized(str(self.current_price), 15).rjust(16)
                + str_sized(str(self.purchase_price), 15).rjust(16)
                + str_sized(str(self.page_count), 11).rjust(12)
                + str_sized(str(self.purchase_year), 14).rjust(15)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.page_count}, {self.purchase_price}, {self.purchase_year})'


@Media.register_subclass('movie')
class Movie(Media):
    mediatype = 'movie'
    NEED_DUPLICATES_AMOUNT = False

    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        super().__init__(title, director, purchase_price, purchase_year)
        self.length = int(length)
        self.degree_of_wear = int(degree_of_wear)
        self.update_current_price()

    # FIXME: Double check this method
    def update_current_price(self):
        'This will calculate the value of a movie based on the base value and degree of wear'
        self.current_price = round(super().base_price() * float(f'0.{self.degree_of_wear}'), 2)

    def save(self) -> list:
        return Movie.mediatype, self.title, self.creator, self.length, self.purchase_price, self.purchase_year, self.degree_of_wear

    def __str__(self):
        return (''
                + str_sized(self.title, 29).ljust(30)
                + str_sized(self.creator, 29).rjust(30)
                + str_sized(str(self.current_price), 15).rjust(16)
                + str_sized(str(self.purchase_price), 15).rjust(16)
                + str_sized(str(self.length), 15).rjust(16)
                + str_sized(str(self.purchase_year), 14).rjust(15)
                + str_sized(str(self.degree_of_wear), 15).rjust(16)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.length}, {self.purchase_price}, {self.purchase_year}, {self.degree_of_wear})'


@Media.register_subclass('cd')
class Music_CD(Media):
    mediatype = 'cd'
    NEED_DUPLICATES_AMOUNT = True

    def __init__(self, title, artist, track_count, length, purchase_price):
        super().__init__(title, artist, purchase_price)
        self.track_count = int(track_count)
        self.length = int(length)

    def update_current_price(self, amount=1):
        'This will calculate the price of a cd object based on the amount of similar cds'
        self.current_price = int(round(self.purchase_price / amount))

    def save(self) -> list:
        return Music_CD.mediatype, self.title, self.creator, self.track_count, self.length, self.purchase_price

    def __str__(self):
        return (''
                + str_sized(self.title, 29).ljust(30)
                + str_sized(self.creator, 29).rjust(30)
                + str_sized(str(self.current_price), 15).rjust(16)
                + str_sized(str(self.purchase_price), 15).rjust(16)
                + str_sized(str(self.track_count), 12).rjust(13)
                + str_sized(str(self.length), 16).rjust(17)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.track_count}, {self.length}, {self.purchase_price})'
