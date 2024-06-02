import requests
import matplotlib.pyplot as plt

# TMDb API key
api_key = '3ccdbb5d47ef5182bf6d24ef4b5e8710'

# Base URL for TMDb API
base_url = 'https://api.themoviedb.org/3'

# Function to fetch movie details
def fetch_movie_details(movie_id):
    # Endpoint for movie details
    endpoint = f'/movie/{movie_id}'
    
    # Parameters for the request
    params = {
        'api_key': api_key,
        'language': 'en-US',  # Set to English
    }

    # Making the request to TMDb API
    response = requests.get(base_url + endpoint, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response as JSON
        data = response.json()
        return data
    else:
        print('Error:', response.status_code)
        return None

# Function to plot movie ratings
def plot_movie_ratings(movie_ids):
    # Lists to store movie titles and ratings
    movie_titles = []
    movie_ratings = []

    # Fetching movie details for each movie ID
    for movie_id in movie_ids:
        movie_details = fetch_movie_details(movie_id)
        if movie_details:
            # Extracting movie title and rating data
            title = movie_details.get('title', 'N/A')
            rating = movie_details.get('vote_average', 0)
            
            # Append movie title and rating data to lists
            movie_titles.append(title)
            movie_ratings.append(rating)

    # Plotting the bar chart with improved styling
    plt.figure(figsize=(12, 6))
    plt.barh(movie_titles, movie_ratings, color='red', edgecolor='black')  # Horizontal bar chart
    plt.xlabel('Rating')
    plt.ylabel('Movie Title')
    plt.title('Movie Ratings')
    plt.gca().invert_yaxis()  # Invert y-axis to display top-rated movies at the top
    plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add gridlines for better readability
    plt.tight_layout()

    # Show the plot
    plt.show()


movie_ids = [550, 671, 672, 13, 24428]  # Sample movie IDs
plot_movie_ratings(movie_ids)
