import media
import fresh_tomatoes

# Avatar movie: title,movie_storyline,poster_image,trailer_youtube
avatar = media.Movie(
    "Avatar",
    "On the lush alien world of Pandora live the Na'vi, beings "
    "who appear primitive but are highly evolved.",
    "http://media.hollywood.com/images/679x1000/7037214.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Fast_and_Furious movie: title,movie_storyline,poster_image,trailer_youtube
fast_and_furious = media.Movie(
    "Fast And Furious 8",
    "Fast and furious 8",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_UY1200_CR64,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uisBaTkQAEs")

# Forrest_gump movie: title,movie_storyline,poster_image,trailer_youtube
forrest_gump = media.Movie(
    "Forrest Gump",
    "Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as "
    "disadvantaged, and thanks to his supportive mother (Sally Field), "
    "he leads anything but a restricted life.",
    "https://resizing.flixster.com/k-FrjLlI2q480TP6nx22eQR06-8=/206x305/v1.bTsxMTE3MzY3NztqOzE3NDk5OzEyMDA7ODAwOzEyMDA",  # NOQA
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

# Sets the movies that will be passed to the fresh_tamatoes file
movies = [avatar, fast_and_furious, forrest_gump]

# open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
