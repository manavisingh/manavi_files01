#This is my media.py file which contains the class Movie and its instance names.

import webbrowser

class Movie():
    def __init__(self, title, movie_storyline, movie_poster, movie_youtube_url, movie_rating, movie_cast, more_info):
        self.title = title
        self.movie_storyline = movie_storyline
        self.movie_poster = movie_poster
        self.movie_youtube_url = movie_youtube_url
        self.movie_rating = movie_rating
        self.movie_cast = movie_cast
        self.more_info = more_info

    def show_cast(self):
        for x in self.movie_cast:
            print x
        return ""
        
    def show_trailer(self):
        print "Showing the movie Trailer, Enjoy!"
        webbrowser.open(self.movie_youtube_url)


        
