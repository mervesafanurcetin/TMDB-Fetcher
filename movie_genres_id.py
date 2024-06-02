
import requests

api_key = "3ccdbb5d47ef5182bf6d24ef4b5e8710"
url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"

response = requests.get(url)
data = response.json()

genres = {}
for genre in data["genres"]:
    genres[genre["id"]] = genre["name"]

print(genres)