import requests
import matplotlib.pyplot as plt

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

# Count of movies in each genre
genre_counts = {genre_name: 0 for genre_name in genres.values()}

# Making requests for all movies for each genre ID
for genre_id in genres.keys():
    # Endpoint for movies by genre
    endpoint = '/discover/movie'
    
    # Parameters for the request
    params = {
        'api_key': api_key,
        'language': 'en-US',  # Set to English
        'sort_by': 'popularity.desc',  # Sort by popularity
        'with_genres': genre_id,  # Get movies in this genre
    }

    # Making the request to TMDb API
    response = requests.get(base_url + endpoint, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response as JSON
        data = response.json()

        # Counting movies in this genre
        genre_counts[genres[genre_id]] = data['total_results']
    else:
        print('Error:', response.status_code)

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(genre_counts.values(), labels=genre_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Movies by Genre')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()
