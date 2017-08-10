import webbrowser

""" Need to pass 4 parameters to create movie object
    1. movie_title
    2. movie_storyline
    3.poster_image
    4.trailer_youtube """


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
