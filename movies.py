
import requests

# TMDb API key
api_key = '3ccdbb5d47ef5182bf6d24ef4b5e8710'

# Base URL for TMDb API
base_url = 'https://api.themoviedb.org/3'

# All genres with their IDs and names
genres = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western'
}

# Making requests for all movies for each genre ID
for genre_id in genres.keys():
    # Endpoint for movies by genre
    endpoint = '/discover/movie'
    
    # Parameters for the request
    params = {
        'api_key': api_key,
        'language': 'en-US',  # Set to English
        'sort_by': 'popularity.desc',  # Sort by popularity
        'with_genres': genre_id  # Get movies in this genre
    }

    # Making the request to TMDb API
    response = requests.get(base_url + endpoint, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response as JSON
        data = response.json()

        # Printing details of movies in this genre
        print("Genre:", genres[genre_id])
        for movie in data['results']:
            print("Title:", movie.get('title'))
            print("Release Date:", movie.get('release_date'))
            print("Genres:", ', '.join([genres.get(genre_id, 'N/A') for genre_id in movie.get('genre_ids', [])]))
            print("Overview:", movie.get('overview'))
            
            # Get budget, revenue, and runtime
            movie_details_url = f"{base_url}/movie/{movie['id']}?api_key={api_key}&language=en-US"
            movie_details_response = requests.get(movie_details_url)
            movie_details = movie_details_response.json()
            
            print("Budget:", movie_details.get('budget'))
            print("Revenue:", movie_details.get('revenue'))
            print("Runtime:", movie_details.get('runtime'))
            
            print("Poster Image:", "https://image.tmdb.org/t/p/original" + movie.get('poster_path', 'N/A'))
            print("Backdrop Image:", "https://image.tmdb.org/t/p/original" + movie.get('backdrop_path') if movie.get('backdrop_path') else 'N/A')
            print("Average Rating:", movie.get('vote_average'))
            print("-------------------------------------------")
    else:
        print('Error:', response.status_code)
