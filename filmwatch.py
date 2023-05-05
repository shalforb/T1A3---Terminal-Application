import json

WATCHLIST_FILE = 'watchlist.json'
WATCHED_FILE = 'watched.json'

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

def load_watched():
    try:
        with open(WATCHED_FILE, 'r') as f:
            watched = json.load(f)
    except FileNotFoundError:
        watched = []
    return watched

def save_watched(watched):
    with open(WATCHED_FILE, 'w') as f:
        json.dump(watched, f, indent=2)

def add_film():
    title = input('Enter the title of the film: ')
    genre = input('Enter the genre of the film: ')
    release_date = input('Enter the release date of the film: ')
    watchlist.append({'title': title, 'genre': genre, 'release_date': release_date})
    save_watchlist(watchlist)

def edit_film():
    title = input('Enter the title of the film to edit: ')
    for film in watchlist:
        if film['title'] == title:
            film['genre'] = input('Enter the new genre of the film: ')
            film['release_date'] = input('Enter the new release date of the film: ')
            save_watchlist(watchlist)
            return
    print(f'"{title}" not found in watchlist')

def remove_film():
    title = input('Enter the title of the film to remove: ')
    for film in watchlist:
        if film['title'] == title:
            watchlist.remove(film)
            save_watchlist(watchlist)
            return
    print(f'"{title}" not found in watchlist')

def print_watchlist():
    print('Watchlist:')
    for film in watchlist:
        print(f"{film['title']} ({film['genre']}, {film['release_date']})")

def print_genre(genre):
    print(f'Watchlist ({genre}):')
    for film in watchlist:
        if film['genre'] == genre:
            print(f"{film['title']} ({film['release_date']})")

def print_release_date():
    print('Watchlist (sorted by release date):')
    for film in sorted(watchlist, key=lambda x: x['release_date']):
        print(f"{film['title']} ({film['genre']}, {film['release_date']})")

def mark_watched():
    title = input('Enter the title of the film to mark as watched: ')
    for film in watchlist:
        if film['title'] == title:
            watchlist.remove(film)
            watched.append(film)
            save_watchlist(watchlist)
            save_watched(watched)
            return
    print(f'"{title}" not found in watchlist')

watchlist = load_watchlist()
watched = load_watched()

while True:
    print('Welcome to the Watchlist App')
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
    elif choice == '4':
        print_watchlist()
    elif choice == '5':
        genre = input('Enter the genre to filter by: ')
        print_genre(genre)
    elif choice == '6':
        print_release_date()
    elif choice == '7':
        mark_watched()
    elif choice == '8':
        print('Goodbye!')
        break
    else:
        print('Invalid choice, please try again.')