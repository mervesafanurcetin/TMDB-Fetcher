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

# Dictionary to store average ratings for each genre
genre_avg_ratings = {genre_name: 0 for genre_name in genres.values()}

# Function to calculate average rating for a genre
def calculate_average_rating(genre_id):
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

        # Calculate average rating for this genre
        total_ratings = sum([movie.get('vote_average', 0) for movie in data['results']])
        num_movies = len(data['results'])
        if num_movies != 0:
            return total_ratings / num_movies
        else:
            return 0
    else:
        print('Error:', response.status_code)
        return 0

# Calculate average ratings for each genre
for genre_id, genre_name in genres.items():
    genre_avg_ratings[genre_name] = calculate_average_rating(genre_id)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(genre_avg_ratings.keys(), genre_avg_ratings.values(), color='purple')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.title('Average Ratings by Genre')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines for the y-axis
plt.tight_layout()

# Show the plot
plt.show()
