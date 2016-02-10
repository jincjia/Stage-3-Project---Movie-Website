import fresh_tomatoes
import media

angry  = media.Movie("12 Angry Men",
					 "Following the closing arguments in a murder trial, the 12 members of the jury must deliberate.",
					 "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
					 "https://www.youtube.com/watch?v=fSG38tk6TpI",
					 "8.9/10",
					 "1957")

leon   = media.Movie("Léon: The Professional",
					 "An innocent, 12-year-old girl will revenge for her parents' murder, with the help of an assassin.",
					 "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
					 "https://www.youtube.com/watch?v=DcsirofJrlM",
					 "8.6/10",
					 "1994")

love   = media.Movie("Love Actually",
					 "Nine intertwined stories, all set during a month before Christmas, examine the complexities of love.",
					 "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",
					 "https://www.youtube.com/watch?v=KdzH6a-XEGM",
					 "7.7/10",
					 "2003")

fox    = media.Movie("Fantastic Mr.Fox",
					 "An urbane fox cannot resist returning to his farm and must help his community survive the farmers' retaliation.",
					 "https://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg",
					 "https://www.youtube.com/watch?v=n2igjYFojUo",
					 "7.8/10",
					 "2009")

food   = media.Movie("Food, Inc.",
					 "This documentary lifts the veil on our nation's food industry, exposing the highly mechanized underbelly.",
					 "https://upload.wikimedia.org/wikipedia/en/a/a8/Food_inc.jpg",
					 "https://www.youtube.com/watch?v=5eKYyD14d_0",
					 "7.9/10",
					 "2009")

up     = media.Movie("Up",
					 "A 78-year-old man finally fulfills his lifelong dream, but an overly optimistic 8-year-old tags along to his surprise.",
					 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
					 "https://www.youtube.com/watch?v=pkqzFUhGPJg",
					 "8.3/10",
					 "2009")

silver = media.Movie("Silver Linings Playbook",
					 "A depressed Eagles fan tries to rebuild his life after a divorce and encounters a sassy ball-room dance enthusiast.",
					 "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",
					 "https://www.youtube.com/watch?v=Lj5_FhLaaQQ",
					 "7.8/10",
					 "2012")

boyhood= media.Movie("Boyhood",
					 "This is a story of growing up as seen through the eyes of a child, filmed over 12 years with the same cast.",
					 "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
					 "https://www.youtube.com/watch?v=Y0oX0xiwOv8",
					 "8.0/10",
					 "2014")

inside = media.Movie("Inside Out",
					 "Growing up can be a bumpy road, and this is a story about how a girl and her five emotions struggle to adjust to a new life.",
					 "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
					 "https://www.youtube.com/watch?v=seMwpP0yeu4",
					 "8.3/10",
					 "2015")

movies = [angry, leon, love, fox, food, up, silver, boyhood, inside]

fresh_tomatoes.open_movies_page(movies)
