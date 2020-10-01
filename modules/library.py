import datetime

from modules.utils import fixed_string


class Lib:
    """Creates the library object
    """
    def __init__(self):
        self.media = []

    def update_prices(self):
        """Updates prices of all objects in library
        """
        for elm in self.media:
            if elm.NEED_DUPLICATES_AMOUNT:
                elm.update_current_price(self.find_duplicates(elm))
            else:
                elm.update_current_price()

    def find_duplicates(self, item):
        """Find duplicates of object in list of objects

        Args:
            item (Media): Media object that you want to find duplicates of

        Returns:
            int: amount of duplicates found
        """
        count = 0
        for elm in self.media:
            if item.NEED_DUPLICATES_AMOUNT:
                if elm.title == item.title and elm.creator == item.creator:
                    count += 1
            else:
                count = None
        return count


class Media:
    """Creates the media object
    """
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
        """Calculates a base price based on the age of the object

        Args:
            age (int, optional): the age of the object. Defaults to None.

        Returns:
            float: the new base price of the object
        """
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
    """Creates the Book subclass of Media

    Args:
        Media (Class): parent class of Book
    """
    mediatype = 'book'
    NEED_DUPLICATES_AMOUNT = False

    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        super().__init__(title, author, purchase_price, purchase_year)
        self.page_count = int(page_count)

    def update_current_price(self):
        """
        Updates current price of this instance.
        If it is older than 50 years the value increases
        """
        price = self.purchase_price
        if self.age > 50:
            price = super().base_price(50)
            for year in range(51, self.age+1):
                price = price * 1.08
                self.current_price = round(price, 2)
        else:
            price = super().base_price()
            self.current_price = round(price, 2)

    def save(self):
        """Returns tuple of data to be sent to file

        Returns:
            tuple: the attributes that is needed to recreate this instance
        """
        return Book.mediatype, self.title, self.creator, self.page_count, self.purchase_price, self.purchase_year

    def __str__(self):
        return (''
                + fixed_string(self.title, 29).ljust(30)
                + fixed_string(self.creator, 29).rjust(30)
                + fixed_string(str(self.current_price), 15).rjust(16)
                + fixed_string(str(self.purchase_price), 15).rjust(16)
                + fixed_string(str(self.page_count), 11).rjust(12)
                + fixed_string(str(self.purchase_year), 14).rjust(15)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.page_count}, {self.purchase_price}, {self.purchase_year})'


@Media.register_subclass('movie')
class Movie(Media):
    """Creates the Movie subclass of Media

    Args:
        Media (Class): parent class of Movie
    """
    mediatype = 'movie'
    NEED_DUPLICATES_AMOUNT = False

    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        super().__init__(title, director, purchase_price, purchase_year)
        self.length = int(length)
        self.degree_of_wear = int(degree_of_wear)
        self.update_current_price()

    def update_current_price(self):
        """
        Updates current price of this instance.
        The value is based on age and wear of the physical object
        """
        self.current_price = round(super().base_price() * float(f'0.{self.degree_of_wear}'), 2)

    def save(self):
        """Returns tuple of data to be sent to file

        Returns:
            tuple: the attributes that is needed to recreate this instance
        """
        return Movie.mediatype, self.title, self.creator, self.length, self.purchase_price, self.purchase_year, self.degree_of_wear

    def __str__(self):
        return (''
                + fixed_string(self.title, 29).ljust(30)
                + fixed_string(self.creator, 29).rjust(30)
                + fixed_string(str(self.current_price), 15).rjust(16)
                + fixed_string(str(self.purchase_price), 15).rjust(16)
                + fixed_string(str(self.length), 15).rjust(16)
                + fixed_string(str(self.purchase_year), 14).rjust(15)
                + fixed_string(str(self.degree_of_wear), 15).rjust(16)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.length}, {self.purchase_price}, {self.purchase_year}, {self.degree_of_wear})'


@Media.register_subclass('cd')
class Music_CD(Media):
    """Creates the Music_CD subclass of Media

    Args:
        Media (Class): parent class of Music_CD
    """
    mediatype = 'cd'
    NEED_DUPLICATES_AMOUNT = True

    def __init__(self, title, artist, track_count, length, purchase_price):
        super().__init__(title, artist, purchase_price)
        self.track_count = int(track_count)
        self.length = int(length)

    def update_current_price(self, amount=1):
        """
        Updates current price of this instance.
        The value is based on the amount of duplicates of this instance
        """
        self.current_price = int(round(self.purchase_price / amount))

    def save(self):
        """Returns tuple of data to be sent to file

        Returns:
            tuple: the attributes that is needed to recreate this instance
        """
        return Music_CD.mediatype, self.title, self.creator, self.track_count, self.length, self.purchase_price

    def __str__(self):
        return (''
                + fixed_string(self.title, 29).ljust(30)
                + fixed_string(self.creator, 29).rjust(30)
                + fixed_string(str(self.current_price), 15).rjust(16)
                + fixed_string(str(self.purchase_price), 15).rjust(16)
                + fixed_string(str(self.track_count), 12).rjust(13)
                + fixed_string(str(self.length), 16).rjust(17)
                )

    def __repr__(self):
        return f'{self.mediatype}(\"{self.title}\", \"{self.creator}\", {self.track_count}, {self.length}, {self.purchase_price})'
