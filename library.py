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
        
#Felhantering för om json filen inte finns på användarens dator, om json filen är tom utan den initiella [] eller om filen finns.
    def Load_DVD_Movies(self):
        # Kontrollera om filen finns
        if os.path.exists(self.Filename):
            try:
                with open(self.Filename, "r") as File:
                    data = File.read().strip()
                    if data:  # Om filen inte är tom
                        self.DVD_movies = [DVD(**Movie) for Movie in json.loads(data)]
                    else:
                        # Filen är tom, skapa en tom lista
                        print("Filen är tom. Skapar en tom lista.")
                        self.DVD_movies = []
            except json.JSONDecodeError:
                print("Ogiltigt JSON-format. Återställer filen.")
                self.DVD_movies = []
            else:
                # Om ingen exception inträffade
                print("Fil laddades korrekt.")
        else:
            # Filen finns inte, skapa en tom lista och spara
            print("Filen finns inte. Skapar en ny JSON-fil.")
            self.DVD_movies = []
            self.Save_DVD_Movies()
        
#Funktion som sparar de ändringar som gjorts till filmerna i biblioteket.
    def Save_DVD_Movies(self):
        with open(self.Filename, "w") as File:
            json.dump([Movie.__dict__ for Movie in self.DVD_movies], File)

#Funktion för att visa användaren de filmer som finns i biblioteket.
    def Show_Library(self):
        for DVD in self.DVD_movies:
            print(DVD.Show_info())

#Funktion för att ta bort filmer ur biblioteket.
    def Remove_DVD_Movie(self, title):
        for i, movie in enumerate(self.DVD_movies):
            if movie.Title.lower() == title.lower():
                del self.DVD_movies[i]
                self.Save_DVD_Movies()
                return True
        return False

#Skapar ett antal fördefinerade filmer.
dvd_library = Library()
movie1 = DVD("The Matrix", ["Lana Wachowski", "Lilly Wachowski"], "Sci-Fi", 1999)
movie2 = DVD("Inception", ["Christopher Nolan"], "Sci-Fi", 2010)
movie3 = DVD("The Godfather", ["Francis Ford Coppola"], "Crime", 1972)
movie4 = DVD("Pulp Fiction", ["Quentin Tarantino"], "Crime", 1994)
dvd_library.Add_DVD_movie(movie1)
dvd_library.Add_DVD_movie(movie2)
dvd_library.Add_DVD_movie(movie3)
dvd_library.Add_DVD_movie(movie4)