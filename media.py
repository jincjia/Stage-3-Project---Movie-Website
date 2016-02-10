import webbrowser
from datetime import date

class Movie():
	""" This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rating, release_year):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_rating = imdb_rating
		self.release_year = release_year

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


