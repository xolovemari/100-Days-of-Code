import requests
from datetime import datetime
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify

# constants
CLIENT_ID = "example"
CLIENT_SECRET = "example"
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
CACHE_PATH = "day 46/.cache"

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_billboard_songs(target_date):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
        }
    URL = f"https://www.billboard.com/charts/hot-100/{target_date}/"

    try:
        response = requests.get(URL, headers=header)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Error acessing Billboard: {e}")
    
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    song_names = [song.getText().strip() for song in soup.select("li ul li h3")]
    
    return song_names

def setup_spotify_client():
    return Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path=CACHE_PATH,
        username="xolovemari"
    )
)

def search_track_uri(sp_client, song_name, year):
    clean_name = (
        song_name.split("(")[0]
        .split("[")[0]
        .strip()
        .replace("'", "")
        .replace("&", "and")
    )

    try:
        result = sp_client.search(
            q=f"track:{clean_name} year:{year}",
            type="track",
            limit=1
        )
        return result["tracks"]["items"][0]["uri"]
    except (IndexError, KeyError):
        print(f"⚠️ Song wasn't found: {clean_name}")
        return None

def main():
    while True:
        date_input = input("Which date do you want to travel to? (YYYY-MM-DD): ")
        if is_valid_date(date_input):
            break
        print("Invalid format! Please use YYYY-MM-DD.")
    
    try:
        songs = get_billboard_songs(date_input)
    except Exception as e:
        print(f"❌ Error getting data: {e}")
        return

    sp = setup_spotify_client()
    user_id = sp.current_user()["id"]
    year = date_input.split("-")[0]

    track_uris = []
    for song in songs:
        if uri := search_track_uri(sp, song, year):
            track_uris.append(uri)

    if track_uris:
        playlist = sp.user_playlist_create(
            user=user_id,
            name=f"{date_input} Billboard 100",
            public=False,
        )
        sp.playlist_add_items(playlist["id"], track_uris)
        print(f"🎉 Successfuly created playlist: {playlist['external_urls']['spotify']}")
    else:
        print("❌ No songs found to create playlist.")


if __name__ == "__main__":
    main()