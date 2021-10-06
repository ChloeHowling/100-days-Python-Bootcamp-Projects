from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

USER_ID = "e3zymbs23k1a8milazyv3kpsm"
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    ))


# auth_endpoint = "https://accounts.spotify.com/authorize"
#
# auth_params = {
#     "client_id": SPOTIPY_CLIENT_ID,
#     "response_type": "code",
#     "redirect_uri": "http://example.com",
#
# }
# response = requests.get(url=auth_endpoint, )


def main():
    user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

    endpoint = "https://www.billboard.com/charts/hot-100/"

    response = requests.get(url=f"{endpoint}{user_input}")
    response.raise_for_status()

    print(response)

    billboard_soup = BeautifulSoup(response.text, "html.parser")

    song_class = "chart-element__information__song text--truncate color--primary"
    song_data = billboard_soup.find_all(name="span", class_=song_class)

    song_list = []
    for song in song_data:
        song_list.append(song.getText().split('/')[0].split('(')[0])
    print(f"List of songs from {user_input} retrieved")
    url_list = []
    for song in song_list:
        track = sp.search(q=song, limit=1, type="track")
        if track['tracks']['items']:
            url = track['tracks']['items'][0]['uri']
            url_list.append(url)
        else:
            print(f"{song} doesn't exist in Spotify. Skipped")
    print("uri list created")

    playlist_name = f"{user_input} Billboard 100"
    playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False)

    print(sp.playlist_add_items(playlist_id=playlist['id'], items=url_list))


main()
