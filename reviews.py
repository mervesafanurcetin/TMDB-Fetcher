
import requests

# TMDb API key
api_key = "3ccdbb5d47ef5182bf6d24ef4b5e8710"

# Function to fetch reviews for a movie
def fetch_reviews(movie_id):
    # TMDb API endpoint for fetching reviews
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    
    # Parameters for the request
    params = {
        'api_key': api_key,
    }
    
    # Make the API request
    response = requests.get(endpoint, params=params)
    
    # Check the response status
    if response.status_code == 200:
        # Process the response as JSON
        data = response.json()
        
        # Extract reviews
        reviews = data["results"]
        
        # Print the reviews
        print(f"Reviews for Movie ID: {movie_id}")
        if reviews:
            for review in reviews:
                print(f"Author: {review['author']}")
                print(f"Content: {review['content']}")
                print("-----------------------------------")
        else:
            print("No reviews found.")
    else:
        print(f"Error fetching reviews for Movie ID {movie_id}. Status code: {response.status_code}")

# Movie IDs for which reviews will be fetched
movie_ids = [823464, 1094844, 693134, 1096197, 1011985, 934632, 940721, 748783, 845111, 1041613, 821937, 1063879, 653346, 976906, 618588, 634492, 359410, 872585, 940551, 784651]

# Fetch reviews for each movie
for movie_id in movie_ids:
    fetch_reviews(movie_id)
