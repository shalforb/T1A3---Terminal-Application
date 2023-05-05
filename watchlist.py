import json

# Function to load the watchlist from a JSON file
def load_watchlist():
    try:
        with open("watchlist.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Function to save the watchlist to a JSON file
def save_watchlist(watchlist):
    with open("watchlist.json", "w") as f:
        json.dump(watchlist, f, indent=4)