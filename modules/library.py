import datetime


class Lib:
    def __init__(self):
        self.media = []

    def add_media(self, input_data):
        print(input_data)
        if input_data[0] == 'b':
            self.media.append(Book(*input_data[1:]))
            print('Book added')
        elif input_data[0] == 'm':
            self.media.append(Movie(*input_data[1:]))
            print('Movie added')
        elif input_data[0] == 'c':
            self.media.append(Music_CD(*input_data[1:]))
            print('Music CD added')
        else:
            print('Something went wrong')

    def show(self, sort='title'):
        books = []
        movies = []
        cds = []
        if sort == 'title':
            sort_index = 0
        elif sort == 'price':
            sort_index = 1
        for x in self.media:
            if isinstance(x, Book):
                books.append((x.title, x.current_price, x))
            if isinstance(x, Movie):
                movies.append((x.title, x.current_price, x))
            if isinstance(x, Music_CD):
                cds.append((x.title, x.current_price, x))
        print('\nBooks')
        print('------------')
        books = sorted(books, key=lambda x: x[sort_index])
        for book in books:
            print(book[2])
        print('\nMovies')
        print('------------')
        movies = sorted(movies, key=lambda x: x[sort_index])
        for movie in movies:
            print(movie[2])
        print('\nMusic CDs')
        print('------------')
        cds = sorted(cds, key=lambda x: x[sort_index])
        for cd in cds:
            print(cd[2])

    def to_dict(self) -> dict:
        'Return a dict with {books, movies, cds}'
        books = []
        movies = []
        music_cds = []
        temp_dict = {}
        for elm in self.media:
            if isinstance(elm, Book):
                books.append(vars(elm))
            elif isinstance(elm, Movie):
                movies.append(vars(elm))
            elif isinstance(elm, Music_CD):
                music_cds.append(vars(elm))
        temp_dict['books'] = books
        temp_dict['movies'] = movies
        temp_dict['music_cds'] = music_cds
        return temp_dict

    def update_prices(self):
        for elm in self.media:
            if isinstance(elm, Music_CD):
                count = 0
                for x in self.media:
                    if isinstance(elm, Music_CD):
                        if x.title == elm.title and x.creator == elm.creator:
                            count += 1
                print(count)
                elm.update_current_price(count)
            else:
                elm.update_current_price()
        print('Prices have been updated')

    def __repr__(self):
        # return [x for x in self.media]
        return self.media

    def __str__(self):
        prod = "\n".join(self.media)
        return prod


class Media:
    def __init__(self, title, creator, purchase_price, purchase_year=None):
        self.title = title
        self.creator = creator
        self.purchase_price = purchase_price
        self.current_price = purchase_price
        if purchase_year is not None:
            self.purchase_year = purchase_year
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
                price = price * 1.08
                self.current_price = round(price, 2)
        else:
            price = super().base_price()
            self.current_price = round(price, 2)

    def save(self) -> list:
        return [{self.title}, {self.creator}, {self.page_count}, {self.purchase_price}, {self.purchase_year}]

    def __str__(self):
        # return f'Title: {self.title}, Author: {self.creator}, Current Price: {self.current_price}, Page Count: {self.page_count},
        # Purchase Price: {self.purchase_price}, Purchase Year: {self.purchase_year}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.page_count}, {self.purchase_year},  {self.age})'

    def __repr__(self):
        return f'{self.__class__.__name__}(\"{self.title}\", \"{self.creator}\", {self.page_count}, {self.purchase_price}, {self.purchase_year})'


class Movie(Media):
    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        super().__init__(title, director, purchase_price, purchase_year)
        self.length = length
        self.degree_of_wear = degree_of_wear
        self.update_current_price()

    def update_current_price(self):
        'This will calculate the value of a movie based on the base value and degree of wear'
        self.current_price = round(super().base_price() * float(f'0.{self.degree_of_wear}'), 2)

    def save(self) -> list:
        return [{self.title}, {self.creator}, {self.length}, {self.purchase_price}, {self.purchase_year}, {self.degree_of_wear}]

    def __str__(self):
        # return f'Title: {self.title}, Director: {self.creator}, Current Price: {self.current_price}, Length: {self.length}, Purchase Price: {self.purchase_price},
        # Purchase Year: {self.purchase_year}, Degree of wear: {self.degree_of_wear}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.length}, {self.purchase_year}, {self.age}, {self.degree_of_wear})'

    def __repr__(self):
        return f'{self.__class__.__name__}(\"{self.title}\", \"{self.creator}\", {self.length}, {self.purchase_price}, {self.purchase_year}, {self.degree_of_wear})'


class Music_CD(Media):
    def __init__(self, title, artist, track_count, length, purchase_price):
        super().__init__(title, artist, purchase_price)
        self.track_count = track_count
        self.length = length
        self.amount = 1  # FIXME: I might be redundant

    def update_current_price(self, amount=1):
        'This will calculate the price of a cd object based on the amount of similar cds'
        self.current_price = int(round(self.purchase_price / amount))

    def save(self) -> list:
        return [{self.title}, {self.creator}, {self.track_count}, {self.length}, {self.purchase_price}]

    def __str__(self):
        # return f'Title: {self.title}, Artist: {self.creator}, Current Price: {self.current_price}, Track Count: {self.track_count}, Length: {self.length}, Purchase Price: {self.purchase_price}'
        return f'{self.__class__.__name__}({self.title}, {self.creator}, {self.purchase_price}, {self.current_price}, {self.track_count},  {self.length})'

    def __repr__(self):
        return f'{self.__class__.__name__}(\"{self.title}\", \"{self.creator}\", {self.track_count}, {self.length}, {self.purchase_price})'
