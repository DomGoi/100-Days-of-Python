import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID=os.environ("ID_Client")
SPOTIPY_CLIENT_SECRET=os.environ("Client_Secret")
USER_ID_SPOTIFY=os.environ("user_spotify")
URL_POST_ENDPOINT=f"https://api.spotify.com/v1/users/{USER_ID_SPOTIFY}/playlists"


date_input=input("What date you want to go back to? format:YYYY-MM-DD").strip()
year_song=date_input.split("-")[0]


URL=f"https://www.billboard.com/charts/hot-100/{date_input}/"

content=requests.get(url=URL)
content.raise_for_status()
code_content=content.text


soup=BeautifulSoup(code_content, "html.parser")

title=soup.select("li ul li h3")
authors=soup.find_all("span", class_="c-label")
song=[song.getText().strip() for song in title]
#singers=[singer.getText().strip() for singer in authors]
print(song)

#print(singers)

# Create a Spotify API Client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="https://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Dominika Goik"
    )
)
user_id=sp.current_user()["id"]

song_uri=[]

for son in song:
    results=sp.search(q=f"type:{son}, year{year_song}",type="track")

    try:
        song_uri_1=results["tracks"]["items"][0]["uri"]
        song_uri.append(song_uri_1)
    except:
        print(f"The song {son} wasn't found in the base.")

print(song_uri)

playlist_name=f"{date_input} Billboard 100"
playlist=sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
