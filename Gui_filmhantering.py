import tkinter as tk  
from tkinter import simpledialog
from dvd import *
from library import *

library = Library()

#Bestämmer dimensionerna av fönstret.
root = tk.Tk()
root.geometry("800x400")
root.title("Movie Library")

#Välkomstmeddelande
title = tk.Label(root, text="Welcome to the movie-library!", font=("Times New Roman", 20))
title.pack()
movie_list = tk.Listbox(root)
movie_list.insert(0)
movie_list.forget()

#Funktion som definerar vad som ska hända om man klickar på "Show DVD's" knappen
def Show_library():
    movie_list.delete(0, tk.END)
    if library.DVD_movies:
        for movie in library.DVD_movies:
            movie_list.insert(tk.END, movie.Title)
    movie_list.pack()

#Funktion som definerar vad som ska hända om man klickar på "Add DVD" knappen
def Add_DVD():
    title_dvd = simpledialog.askstring("Enter Title", "Please enter the title for the DVD", parent=root)
    nmbr_directors = simpledialog.askinteger("Number of directors", "How many directors does the movie have? (enter a number)", parent=root)
    directors = []
    for director in range (nmbr_directors):
        director_dvd = simpledialog.askstring("Enter Director", "Please enter the director name", parent=root)
        directors.append(director_dvd.capitalize())
    genre_dvd = simpledialog.askstring("Enter the genre", "What genre is the movie?", parent=root)
    year_dvd = simpledialog.askinteger("Enter production year", "What year was the movie produced?", parent=root)
    new_dvd = DVD(title_dvd.capitalize(), directors, genre_dvd.capitalize(), year_dvd)
    library.Add_DVD_movie(new_dvd)
    library.Save_DVD_Movies()

#Funktion som definerar vad som ska hända om man klickar på "Remove DVD" knappen.
def Remove_DVD():
    rmv_dvd = simpledialog.askstring("Enter title to remove", "Please enter the title of the movie you want to remove.")
    popup = tk.Toplevel()
    label = tk.Label(popup, text="Movie was removed sucessfully")
    label.pack()
    library.Remove_DVD_Movie(rmv_dvd)
    library.Save_DVD_Movies()

#Skapar en knapp för att aktivera show library funktionen vilket visar de DVD filmer som finns i biblioteket.
show_button = tk.Button(root, text="Show Library", font=("Times New Roman", 12), command=Show_library)
show_button.pack()

#Skapar en knapp för att aktivera add dvd funktionen som låter användaren lägga till en ny film.
add_button = tk.Button(root, text="Add DVD", font=("Times New Roman", 12), command=Add_DVD)
add_button.pack()

#Skapar en knapp för att aktivera remove dvd funktionen som låter användaren radera en av dvd filmerna.
remove_button = tk.Button(root, text="Remove DVD", font=("Times New Roman", 12), command=Remove_DVD)
remove_button.pack()

#En knapp för att avsluta programmet.
quit_button = tk.Button(root, text="Quit", font=("Times New Roman", 12), command=exit)
quit_button.pack()
    

root.mainloop()