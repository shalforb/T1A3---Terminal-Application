import imdb
ia = imdb.Cinemagoer()

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