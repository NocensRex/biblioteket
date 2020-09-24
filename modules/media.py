class Media:
    def __init__(self, title, purchase_price):
        self.title = title
        self.purchase_price = purchase_price
        self.current_price = purchase_price
    
    def __repr__(self):
        pass


class Book(Media):
    def __init__(self, title, author, page_count, purchase_price, purchase_year):
        super().__init__(title, purchase_price)
        self.author = author
        self.page_count = page_count
        self.purchase_year = purchase_year


class Movie(Media):
    def __init__(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        super().__init__(title, purchase_price)
        self.director = director
        self.length = length
        self.purchase_year = purchase_year
        self.degree_of_wear = degree_of_wear


class Music_CD(Media):
    def __init__(self, title, artist, track_count, length, purchase_price):
        super().__init__(title, purchase_price)
        self.artist = artist
        self.track_count = track_count
        self.length = length

