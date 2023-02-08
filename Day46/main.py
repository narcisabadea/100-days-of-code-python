import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from configparser import ConfigParser


travel_date = input(
    "Which yeah do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_date}/"


# Scrap billboard.com for the top songs from the entered date

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select("li #title-of-a-story")
song_titles = [song.getText(strip=True) for song in songs]

artists = soup.find_all(name="span", class_="u-max-width-330")
artist_names = [name.getText().strip("\n\t") for name in artists]

song_and_artist = dict(zip(song_titles, artist_names))

print(song_and_artist)
print()
print("Searching for songs on Spotify and creating new playlist...")

# Spotify Authentication


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    return config["spotify"]


SPOTIFY_KEYS = _get_api_key()
CLIENT_ID = SPOTIFY_KEYS["CLIENT_ID"]
CLIENT_SECRET_ID = SPOTIFY_KEYS["CLIENT_SECRET_ID"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

#  Create a list of Spotify song URIs for the list of song names you found from scraping billboard 100
song_uris = []
for (song, artist) in song_and_artist.items():
    try:
        result = sp.search(q=f"track:{song} artist:{artist}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        pass

print(f"Number of songs found: {len(song_uris)}")

# Create a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{travel_date} Billboard 100", public=False, )

# Add songs found into new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(
    f"New playlist '{travel_date} Billboard 100' successfully created on Spotify!")
