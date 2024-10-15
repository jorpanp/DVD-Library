import json
import os
from dvd import *

#Klass Library som sparar en massa DVD-klasser i ett json dokument som heter dvd_library.
class Library:
    def __init__(self, Filename="dvd_library.json"):
        self.Filename = Filename
        self.DVD_movies = []
        if os.path.exists(self.Filename):
            self.Load_DVD_Movies()

#Funktion som hanterar tilläggning av nya DVD filmer.
    def Add_DVD_movie(self, DVD):
        if any(DVD.Title == f.Title for f in self.DVD_movies):
            return False
        else:
            self.DVD_movies.append(DVD)
            self.Save_DVD_Movies()
            return True
        
#Funktion som listar existerande filmer i biblioteket.
    def Load_DVD_Movies(self):
        with open(self.Filename, "r") as File:
            self.DVD_movies = [DVD(**Movie) for Movie in json.load(File)]

    def Save_DVD_Movies(self):
        with open(self.Filename, "w") as File:
            json.dump([Movie.__dict__ for Movie in self.DVD_movies], File)

    def Show_Library(self):
        for DVD in self.DVD_movies:
            print(DVD.Show_info())

    def Remove_DVD_Movie(self, title):
        for i, movie in enumerate(self.DVD_movies):
            if movie.Title.lower() == title.lower():
                del self.DVD_movies[i]
                self.Save_DVD_Movies()
                return True
        return False
