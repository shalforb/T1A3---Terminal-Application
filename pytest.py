import pytest
import json
from filmtracker import load_watchlist, save_watchlist, add_film, remove_film

WATCHLIST_FILE = 'watchlist.json'

def test_add_film():
    # Create an empty watchlist file
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump([], f)

    # Add a film to the watchlist
    add_film()
    watchlist = load_watchlist()
    assert len(watchlist) == 1
    assert watchlist[0]['title'] == 'Test Movie'
    assert watchlist[0]['genre'] == 'Action'
    assert watchlist[0]['release_date'] == 2023

    # Add another film to the watchlist
    add_film()
    watchlist = load_watchlist()
    assert len(watchlist) == 2

def test_remove_film():
    # Create a watchlist file with two films
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump([
            {
                'title': 'Test Movie 1',
                'genre': 'Action',
                'release_date': 2023
            },
            {
                'title': 'Test Movie 2',
                'genre': 'Comedy',
                'release_date': 2022
            }
        ], f)

    # Remove a film from the watchlist
    remove_film()
    watchlist = load_watchlist()
    assert len(watchlist) == 1
    assert watchlist[0]['title'] == 'Test Movie 2'
    assert watchlist[0]['genre'] == 'Comedy'
    assert watchlist[0]['release_date'] == 2022

    # Try to remove a film that doesn't exist
    with pytest.raises(SystemExit):
        remove_film()