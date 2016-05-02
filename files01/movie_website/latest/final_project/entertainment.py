#This is my entertainment.py file which contains the list of my favourite movies and their information

import fresh_tomatoes
import media

notebook = media.Movie("Notebook",
                       "A Love Story",
                       "http://orig12.deviantart.net/d8f3/f/2010/151/8/c/fan_poster_the_notebook_by_amidsummernights.jpg",
                       "https://www.youtube.com/watch?v=Kp5BSBoOw8k",
                       "4 (Out of 5)",
                       ["Ryan_Gosling","Rachel McAdams"],
                       "https://en.wikipedia.org/wiki/The_Notebook_(2004_film)")

movies = [notebook]

print fresh_tomatoes.open_movies_page(movies)
#print notebook.movie_rating
#print notebook.show_cast()
#print notebook.show_trailer()  
