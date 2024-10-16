from library import *
from dvd import *
 
#Main program som hanterar användarinput i terminalen.
def main():
    library = Library()

    while True:
        print("--- DVD Library ---")
        print("1. Show library")
        print("2. Add new DVD")
        print("3. Remove DVD")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            library.Show_Library()

        elif choice == "2":
            title = input("Enter the title of the DVD: ").capitalize()
            directors_input = input("Enter the name of the director. If there are more than one please separate the two names with a comma.: ")
            directors = [director.strip().capitalize() for director in directors_input.split(",")]
            genre = input("Enter the genre: ").capitalize()
            year = input("Enter the production year: ")

            New_DVD = DVD(title, directors, genre, int(year))
            
            if library.Add_DVD_movie(New_DVD):
                print(f"{title} has been added successfully.")
            else:
                print("That movie already exists in the library")

        elif choice == "3":
            Title_to_remove = input("Enter the title of the DVD you want to remove: ")
            if library.Remove_DVD_Movie(Title_to_remove):
                print(f"{Title_to_remove} has been removed from the library.")
            else:
                print("That movie was not found in the library.")

        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Plese choose again: ")

main()