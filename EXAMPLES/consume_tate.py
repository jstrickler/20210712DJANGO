import requests

tate_url = "http://localhost:8000/api/artists-cbv?name=smith"

response = requests.get(tate_url)

artist_data = response.json()

for artist in artist_data:
    print("{} {}".format(artist.get('name'), artist.get('birth_year')))
