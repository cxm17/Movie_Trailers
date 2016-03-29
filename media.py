"""
Module containing class used to build movie trailer website.

Classes:
    Movie - object with attributes of title, storyline, trailer video and poster art.

"""
import webbrowser

class Movie():
    """ Store texual and multimedia attributes related to describing an individual movie. 

    Constructors:
        __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)__init__ 
    Public Methods:
        show_trailer(self) 
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Build Movie object containing attributes (in order):
            1. Title - The name of the film
            2. Storyline - brief description of the film
            3. URL of poster image art
            4. URL of film trailer 
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        """Open webbroswer using URL value provided for the film trailer during object construction (uses Python webbrowser module)."""
        webbrowser.open(self.trailer_youtube_url) # Python provided BIF
