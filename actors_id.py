
import requests

# TMDb API key
api_key = "3ccdbb5d47ef5182bf6d24ef4b5e8710"

# TMDb API endpoint
endpoint = "https://api.themoviedb.org/3/person/popular"

# Parameters for the request
params = {
    'api_key': api_key,
    'language': 'en-US',
    'page': 1  # Page number 
}

# Create a list to store all actor IDs
all_actor_ids = []

# Loop to get actor IDs from all pages
while True:
    # Make the API request
    response = requests.get(endpoint, params=params)

    # Check the API response
    if response.status_code == 200:
        # Process the response as JSON
        data = response.json()
        
        # Extract actor IDs and add them to the list
        actor_ids = [actor['id'] for actor in data['results']]
        all_actor_ids.extend(actor_ids)
        
        # Check if there is another page
        if data['page'] < data['total_pages']:
            params['page'] += 1
        else:
            break
    else:
        print('Error:', response.status_code)
        break

# Print the results
print("Total number of actors:", len(all_actor_ids))
print("First 10 actor IDs:")
for actor_id in all_actor_ids[:10]:
    print(actor_id)

