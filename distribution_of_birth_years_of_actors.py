import requests
import matplotlib.pyplot as plt

# TMDb API key
api_key = "3ccdbb5d47ef5182bf6d24ef4b5e8710"

# TMDb API endpoint for fetching actor details
endpoint = "https://api.themoviedb.org/3/person/"

# Function to fetch actor information
def fetch_actor_info(actor_id):
    # Parameters for the request
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    
    # Make the API request
    response = requests.get(endpoint + str(actor_id), params=params)
    
    # Check the response status
    if response.status_code == 200:
        # Process the response as JSON
        data = response.json()
        
        # Extract actor information
        actor_info = {
            "Name": data["name"],
            "Birthday": data["birthday"],
            "Place of Birth": data["place_of_birth"],
            "Biography": data["biography"],
            "Profile Image": f"https://image.tmdb.org/t/p/original{data['profile_path']}" if data["profile_path"] else "N/A"
        }
        
        return actor_info
    else:
        print(f"Error fetching information for actor ID {actor_id}. Status code: {response.status_code}")
        return None

# Actor IDs to fetch information for
actor_ids = [
    115440,  
    1196101,
    3564806,
    1813,
    12799,
    976,
    989325,
    974169,
    1245,
    31
]

# List to store birth years of actors
birth_years = []

# Fetch information for each actor and extract birth years
for actor_id in actor_ids:
    actor_info = fetch_actor_info(actor_id)
    if actor_info and actor_info["Birthday"]:
        birth_year = int(actor_info["Birthday"].split("-")[0])
        birth_years.append(birth_year)

# Plotting histogram of birth years
plt.hist(birth_years, bins=30, alpha=0.7, color='pink')

# Plot customization
plt.xlabel('Birth Year')
plt.ylabel('Number of Actors')
plt.title('Distribution of Birth Years of Actors')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
