import modules.value as value


class Book():
    """
    A class used to represent a Book

    Attributes
    ----------
    title : str
        the title of the book
    author : str
        the author of the book
    page_count : int
        the number of pages in the book
    purchase_price : float
        the purchase price of the book
    purchase_year : int
        the year the book was bought
    current_value : float
        the current value(price) of the book based on age

    Methods
    -------
    get_all()
        returns all attributes as a list
    set_current_value()
        this updates the current_value
    """
    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        """
        Parameters
        ----------
        title : str
            the title of the book
        author : str
            the author of the book
        page_count : int
            the number of pages in the book
        purchase_price : float
            the purchase price of the book
        purchase_year : int
            the year the book was bought
        current_value : float
            the current value(price) of the book based on age
        """
        self.title = title
        self.author = author
        self.page_count = page_count
        self.purchase_price = purchase_price
        self.purchase_year = purchase_year
        self.current_value = 0

    def get_all(self):
        'Returns a list of all attributes this class has'
        return [self.title, self.author, self.page_count, self.purchase_price, self.purchase_year, self.current_value]

    def set_current_value(self):
        'This updates the current value of the instance.'
        self.current_value = value.book_value(self.purchase_price, self.purchase_year)


class Movie():
    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        self.title = title
        self.director = director
        self.length = length
        self.purchase_price = purchase_price
        self.purchase_year = purchase_year
        self.current_value = 0
        self.degree_of_wear = degree_of_wear

    def get_all(self):
        return self.title, self.director, self.length, self.purchase_price, self.purchase_year, self.current_value

    def set_current_value(self):
        self.current_value = value.movie_value(self.purchase_price, self.purchase_year, self.degree_of_wear)


class Music_CD():
    def __init__(self, title, artist, track_count, length, purchase_price):
        self.title = title
        self.artist = artist
        self.track_count = track_count
        self.length = length
        self.purchase_price = purchase_price
        self.current_value = 0

    def get_all(self):
        return self.title, self.artist, self.track_count, self.length, self.purchase_price, self.current_value

    def set_current_value(self, amount):
        self.current_value = value.cd_value(self.purchase_price, amount)
