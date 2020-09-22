class Book():
    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.purchase_price = purchase_price
        self.purchase_year = purchase_year
        self.current_value = 0

    def get_all(self):
        return self.title, self.author, self.page_count, self.purchase_price, self.purchase_year, self.current_value


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
