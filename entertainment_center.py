import media
import fresh_tomatoes

""" Created three movie object """
avatar = media.Movie("Avatar",
                        "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.",
                        "http://media.hollywood.com/images/679x1000/7037214.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

fast_and_furious = media.Movie("Fast And Furious 8",
                        "Fast and furious 8",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_UY1200_CR64,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=uisBaTkQAEs")

forrest_gump = media.Movie("Forrest Gump",
                        "Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, and thanks to his supportive mother (Sally Field), he leads anything but a restricted life.",
                        "https://resizing.flixster.com/k-FrjLlI2q480TP6nx22eQR06-8=/206x305/v1.bTsxMTE3MzY3NztqOzE3NDk5OzEyMDA7ODAwOzEyMDA",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")

movies = [avatar,fast_and_furious,forrest_gump]

fresh_tomatoes.open_movies_page(movies)
