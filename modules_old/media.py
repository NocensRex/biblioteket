import datetime


class Media:
    def __init__(self, title, creator, purchase_price, purchase_year=None):
        self.title = title
        self.creator = creator
        self.purchase_price = purchase_price
        self.current_price = purchase_price
        if purchase_year is not None:
            self.purchase_year = purchase_year
            self.age = datetime.datetime.today().year - self.purchase_year

    def base_price(self, age=None):
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

    def __repr__(self):
        if self.purchase_year is not None:
            return f'{self.__class__.__name__}({self.title}{self.creator}{self.purchase_price}{self.current_price}{self.purchase_year}{self.age}'
        else:
            return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}'


class Book(Media):
    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        super().__init__(title, author, purchase_price, purchase_year)
        self.page_count = page_count

    def update_current_price(self):
        'This will recalculate the value of a book if it is older than 50 years'
        price = self.purchase_price
        if self.age > 50:
            price = super().base_price(50)
            for year in range(51, self.age+1):
                price = price() * 1.08
                self.current_price = price
        else:
            price = super().base_price()
            self.current_price = price

    def __str__(self):
        # return f'Title: {self.title}, Author: {self.creator}, Current Price: {self.current_price}, Page Count: {self.page_count},
        # Purchase Price: {self.purchase_price}, Purchase Year: {self.purchase_year}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.page_count}, {self.purchase_year},  {self.age})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.page_count}, {self.purchase_price}, {self.purchase_year})'


class Movie(Media):
    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        super().__init__(title, director, purchase_price, purchase_year)
        self.length = length
        self.degree_of_wear = degree_of_wear
        self.update_current_price()

    def update_current_price(self):
        'This will calculate the value of a movie based on the base value and degree of wear'
        self.current_price = round(super().base_price() * float(f'0.{self.degree_of_wear}'), 2)

    def __str__(self):
    #     return f'Title: {self.title}, Director: {self.creator}, Current Price: {self.current_price}, Length: {self.length}, Purchase Price: {self.purchase_price}, Purchase Year: {self.purchase_year}, Degree of wear: {self.degree_of_wear}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.length}, {self.purchase_year}, {self.age}, {self.degree_of_wear})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.length}, {self.purchase_price}, {self.purchase_year}, {self.degree_of_wear})'


class Music_CD(Media):
    def __init__(self, title, artist, track_count, length, purchase_price):
        super().__init__(title, artist, purchase_price)
        self.track_count = track_count
        self.length = length
        self.amount = 1

    def update_current_price(self, amount=1):
        'This will calculate the price of a cd object based on the amount of similar cds'
        self.current_price = int(round(self.purchase_price / amount))

    def __str__(self):
        # return f'Title: {self.title}, Artist: {self.creator}, Current Price: {self.current_price}, Track Count: {self.track_count}, Length: {self.length}, Purchase Price: {self.purchase_price}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.track_count},  {self.length})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.track_count}, {self.length}, {self.purchase_price})'
