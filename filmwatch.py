import json

WATCHLIST_FILE = 'watchlist.json'
WATCHED_FILE = 'watched.json'
watchlist = []

def load_watchlist():
    try:
        with open(WATCHLIST_FILE, 'r') as f:
            watchlist = json.load(f)
    except FileNotFoundError:
        watchlist = []
    return watchlist

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f, indent=2)

def add_film():
    global watchlist # define the watchlist variable as a global variable
    title = input('Enter the title of the film: ')
    genre = input('Enter the genre of the film: ')
    release_date = input('Enter the release date of the film: ')
    watchlist.append({'title': title, 'genre': genre, 'release_date': release_date})
    save_watchlist(watchlist)

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

def remove_film():
    global watchlist # define the watchlist variable as a global variable
    title = input('Enter the title of the film to remove: ')
    for film in watchlist:
        if film['title'] == title:
            watchlist.remove(film)
            save_watchlist(watchlist)
            return
    print(f'"{title}" not found in watchlist')

while True:
    print('Welcome to the FilmApp')
    print('-----------------------------')
    print('1. Add film')
    print('2. Edit film')
    print('3. Remove film')
    print('4. Print watchlist')
    print('5. Print by genre')
    print('6. Print by release date')
    print('7. Mark film as watched')
    print('8. Exit')

    choice = input('Enter your choice (1-8): ')

    if choice == '1':
        add_film()
    elif choice == '2':
        edit_film()
    elif choice == '3':
        remove_film()
    elif choice == '8':
        print('Goodbye!')
        break
    else:
        print('Invalid choice, please try again.')