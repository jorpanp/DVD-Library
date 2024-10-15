import tkinter as tk  
from tkinter import messagebox, simpledialog
from dvd import *
from library import *

library = Library()

#Bestämmer dimensionerna av fönstret.
root = tk.Tk()
root.geometry("800x400")
root.title("Filmhanteraren")

#Välkomstmeddelande
title = tk.Label(root, text="Välkommen till Filmhanteraren!", font=("Times New Roman", 20))
title.pack()
movie_list = tk.Listbox(root)
movie_list.insert(0, "test1")
movie_list.forget()

#Funktion som definerar vad som ska hända om man klickar på "Show DVD's" knappen
def Show_library():
    if library.DVD_movies:
        print(library.Show_Library())
        movie_list.pack()


def Add_DVD():
    title_dvd = simpledialog.askstring("Enter Title", "Please enter the title for the DVD")
    nmbr_directors = simpledialog.askinteger("Number of directors", "How many directors does the movie have? (enter a number)")
    directors = []
    for director in range (nmbr_directors):
        director_dvd = simpledialog.askstring("Enter Director", "Please enter the director name")
        directors.append(director_dvd.capitalize())
    genre_dvd = simpledialog.askstring("Enter the genre", "What genre is the movie?")
    year_dvd = simpledialog.askinteger("Enter production year", "What year was the movie produced?")
    new_dvd = DVD(title_dvd.capitalize(), directors, genre_dvd.capitalize(), year_dvd)
    library.Add_DVD_movie(new_dvd)
    library.Save_DVD_Movies()

def Remove_DVD():
    rmv_dvd = simpledialog.askstring("Enter title to remove", "Please enter the title of the movie you want to remove.")
    popup = tk.Toplevel()
    label = tk.Label(popup, text="Movie was removed sucessfully")
    label.pack()
    library.Remove_DVD_Movie(rmv_dvd)
    library.Save_DVD_Movies()

#Skapar en knapp för att aktivera show library funktionen vilket visar de DVD filmer som finns i biblioteket.
showbtn = tk.Button(root, text="Show Library", command=Show_library)
showbtn.pack()

addbtn = tk.Button(root, text="Add DVD", command=Add_DVD)
addbtn.pack()

rmvbtn = tk.Button(root, text="Remove DVD", command=Remove_DVD)
rmvbtn.pack()

quitbtn = tk.Button(root, text="Quit", command=exit)
quitbtn.pack()
    

root.mainloop()