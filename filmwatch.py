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

