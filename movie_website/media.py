# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self,movie_title,movie_storyline,movie_poster,movie_youtube_url,movie_cast,movie_rating):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.youtube_url = movie_youtube_url
        self.cast = movie_cast
        self.rating = movie_rating

    def video_youtube(self):
        webbrowser.open(self.youtube_url)
        


    


        
