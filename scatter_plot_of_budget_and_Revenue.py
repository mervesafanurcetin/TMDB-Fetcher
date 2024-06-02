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

# Function to plot scatter plot of budget vs. revenue
def plot_budget_vs_revenue(movie_ids):
    # Lists to store budget and revenue data
    budgets = []
    revenues = []

    # Fetching movie details for each movie ID
    for movie_id in movie_ids:
        movie_details = fetch_movie_details(movie_id)
        if movie_details:
            # Extracting budget and revenue data
            budget = movie_details.get('budget', 0)
            revenue = movie_details.get('revenue', 0)
            
            # Append budget and revenue data to lists
            budgets.append(budget)
            revenues.append(revenue)

    # Plotting the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(budgets, revenues, color='red', alpha=0.7)
    plt.xlabel('Budget (in $)')
    plt.ylabel('Revenue (in $)')
    plt.title('Budget vs. Revenue')
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example movie IDs 
movie_ids = [550, 671, 672, 13, 24428]  # Sample movie IDs
plot_budget_vs_revenue(movie_ids)
