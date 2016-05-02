# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
#import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story of a boys's toys which come alive",
                        "http://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "Here is the video",
                        "[a,b,c]",
                        "4.5 (Out of 5)")

#avatar = media.Movie()

#movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)

print toy_story.video_youtube()


