from modules.media import Book, Movie, Music_CD


class Lib:
    def __init__(self):
        self.media = []

    def add_media(self, input_data):
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

    def show(self):
        for x in self.media:
            print(x)

    def __repr__(self):
        # return [x for x in self.media]
        return self.media

    def __str__(self):
        prod = "\n".join(self.media)
        return prod
