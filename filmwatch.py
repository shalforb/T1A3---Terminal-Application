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
