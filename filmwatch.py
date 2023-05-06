import json
from prettytable import PrettyTable
from imdb import Cinemagoer
from datetime import datetime
import sys

WATCHLIST_FILE = 'watchlist.json'
WATCHED_FILE = 'watched.json'
ia = Cinemagoer()

# Function to load the watchlist from a JSON file
def load_watchlist(): 
    try:
        with open(WATCHLIST_FILE, 'r') as f:
            watchlist = json.load(f)
    except FileNotFoundError:
        watchlist = []
    return watchlist

# Function to load the watched list from a JSON file
def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f, indent=2)

# Function to load the watched list from a JSON file
def load_watched():
    try:
        with open(WATCHED_FILE, 'r') as f:
            watched = json.load(f)
    except FileNotFoundError:
        watched = []
    return watched

# Function to save the watched list to a JSON file
def save_watched(watched):
    with open(WATCHED_FILE, 'w') as f:
        json.dump(watched, f, indent=2)

def search_film():
    title = input('Enter the title of the film to search: ')
    results = ia.search_movie(title)

    # Check if any results were found
    if not results:
        print(f'"{title}" not found on IMDb')
        return

    # Print the details of the first result
    movie_id = results[0].movieID
    movie = ia.get_movie(movie_id)
    title = movie.get('title', '')
    genre = ', '.join(movie.get('genres', []))
    release_date = movie.get('year', '')
    print(f'Title: {title}\nGenre: {genre}\nRelease Date: {release_date}')

    # Prompt user to add the movie to their watchlist
    add_to_watchlist = input('Would you like to add this movie to your watchlist? (yes/no) ')
    if add_to_watchlist.lower() == 'yes':
        # Add movie details to JSON file
        with open('watchlist.json', 'a') as f:
            watchlist.append({'title': title, 'genre': genre.split(',')[0].strip(), 'release_date': release_date})
            save_watchlist(watchlist)

# Function to add a film to the watchlist
def add_film():
    global watchlist # define the watchlist variable as a global variable
    title = input('Enter the title of the film: ')
    genre = input('Enter the genre of the film: ')
    release_date = input('Enter the release date of the film: ')
    watchlist.append({'title': title, 'genre': genre, 'release_date': release_date})
    save_watchlist(watchlist)


# Function to edit a film in the watchlist
def edit_film():
    global watchlist # define the watchlist variable as a global variable
    title = input('Enter the title of the film to edit: ')
    for film in watchlist:
        if film['title'] == title:
            film['genre'] = input('Enter the new genre of the film: ')
            film['release_date'] = input('Enter the new release date of the film: ')
            save_watchlist(watchlist)
            return
    print(f'"{title}" not found in watchlist')

# Function to remove a film from the watchlist
def remove_film():
    global watchlist # define the watchlist variable as a global variable
    title = input('Enter the title of the film to remove: ')
    for film in watchlist:
        if film['title'] == title:
            watchlist.remove(film)
            save_watchlist(watchlist)
            return
    print(f'"{title}" not found in watchlist')

# Function to print the watchlist
def print_watchlist():
    global watchlist # define the watchlist variable as a global variable
    print('Watchlist:')
    table = PrettyTable()
    table.field_names = ["Title", "Genre", "Release Date"]
    for film in watchlist:
        table.add_row([film['title'], film['genre'], film['release_date']])
    print(table)

# Function to print films by genre
def print_genre(genre):
    global watchlist  # define the watchlist variable as a global variable
    table = PrettyTable(['Title', 'Release Date'])
    table.align['Title'] = 'l'
    table.align['Release Date'] = 'r'
    table.title = f"Watchlist ({genre})"
    for film in watchlist:
        if film['genre'] == genre:
            table.add_row([film['title'], film['release_date']])
    print(table)

# Function to print films by release date
def print_release_date():
    global watchlist  # define the watchlist variable as a global variable
    table = PrettyTable(['Title', 'Genre', 'Release Date'])
    table.align['Title'] = 'l'
    table.align['Genre'] = 'l'
    table.align['Release Date'] = 'r'
    table.title = "Watchlist (sorted by release date)"
    for film in sorted(watchlist, key=lambda x: x['release_date']):
        table.add_row([film['title'], film['genre'], film['release_date']])
    print(table)

# Function to mark a film as watched

def mark_watched():
    global watchlist  # define the watchlist variable as a global variable
    title = input('Enter the title of the film to mark as watched: ')
    for film in watchlist:
        if film['title'] == title:
            watchlist.remove(film)
            date_str = input('Enter the date (DD-MM-YY) you watched the film: ')
            date = datetime.strptime(date_str, '%d-%m-%y')
            rating = int(input('Enter a rating from 1-5: '))
            film['date'] = date.strftime('%d-%m-%y')
            film['rating'] = rating
            watched.append(film)
            save_watchlist(watchlist)
            save_watched(watched)
            return
    print(f'"{title}" not found in watchlist')

# Function to print the watched films list

def print_watched_list():
    watched = load_watched()
    print('Watched List:')
    table = PrettyTable()
    table.field_names = ["Title", "Genre", "Release Date", "Date Watched", "Rating"]
    for movie in watched:
        title = movie.get('title', '')
        genre = movie.get('genre', '')
        release_date = movie.get('release_date', '')
        date_watched = movie.get('date', '')
        rating = movie.get('rating', '')
        table.add_row([title, genre, release_date, date_watched, rating])
    print(table)

def main():
    # Load watchlist and watched list from JSON files
    global watchlist, watched
    watchlist = load_watchlist()
    watched = load_watched()

    while True:
        print("====================================================================================================================")
        print("=  _______  __   __      .___  ___. .___________..______          ___       ______  __  ___  _______ .______       =")
        print("= |   ____||  | |  |     |   \/   | |           ||   _  \        /   \     /      ||  |/  / |   ____||   _  \      =")
        print("= |  |__   |  | |  |     |  \  /  | `---|  |----`|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |     =")
        print("= |   __|  |  | |  |     |  |\/|  |     |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /      =")
        print("= |  |     |  | |  `----.|  |  |  |     |  |     |  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----. =")  
        print("= |__|     |__| |_______||__|  |__|     |__|     | _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____| =")
        print("====================================================================================================================")
        print("\nWelcome to FilmTracker! Make a selection from the menu below:")
        print("\n1. I'd like to add a film to my watchlist")
        print("2. I'd like to log a film I watched")
        print("3. That'll do, pig.")


        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            print("\n==========================")
            print("= Add a Film to Watchlist =")
            print("==========================")
            print("\n1. Search for a film")
            print("2. Enter film details manually")
            print("3. Edit a film in the watchlist")
            print("4. Remove a film from the watchlist")
            print("5. Print watchlist")
            print("6. Print films by genre")
            print("7. Print films by release date")
            print("8. E.T phone home")

            sub_choice = input("Enter your choice (1-8): ")
            if sub_choice == '1':
                search_film()
            elif sub_choice == '2':
                add_film()
            elif sub_choice == '3':
                edit_film()
            elif sub_choice == '4':
                remove_film()
            elif sub_choice == '5':
                print_watchlist()
            elif sub_choice == '6':
                genre = input("Enter genre to filter by: ")
                print_genre(genre)
            elif sub_choice == '7':
                print_release_date()
            elif sub_choice == '8':
                main()
            else:
                print("Invalid choice, please try again")

        elif choice == '2':
            print("\n==========================")
            print("= Log a Film as Watched   =")
            print("==========================")
            print("\n1. Mark a film as watched")
            print("2. Print watched list")
            print("3. E.T Phone home")

            sub_choice = input("\nEnter your choice (1-3): ")
            if sub_choice == '1':
                mark_watched()
            elif sub_choice == '2':
                print_watched_list()
            elif sub_choice == '3':
                main()
            else:
                print("Invalid choice, please try again")
        elif choice == '3':
            print("Goodbye!")
            sys.exit()  # terminate program
        
        else:
            print("Invalid choice, please try again")

if __name__ == '__main__':
    main()