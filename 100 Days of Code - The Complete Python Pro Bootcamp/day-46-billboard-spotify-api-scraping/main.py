import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

load_dotenv() # This loads variables from .env into os.environ

billboard_base = "https://www.billboard.com/charts/hot-100/"
header = {"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

client_id = os.getenv("SPOTIFY_CLIENT_ID")
# print(f"{client_id}")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
# print(f"{client_secret}")
redirect = os.getenv("SPOTIFY_REDIRECT_URL")
# print(f"{redirect}")
userid = os.getenv("MY_ID")


# day = input("What day would you like to travel to? YYYY-MM-DD")
day = datetime.now()
formatted_date = day.strftime("%Y-%m-%d")
# print(day)

response = requests.get(billboard_base)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_songs = soup.select("div .o-chart-results-list-row-container ul li ul li h3")

# print(all_songs)
song_titles = [song.getText().strip() for song in all_songs]
print(song_titles)

sp = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope="playlist-modify-private")
# token = sp.get_access_token()
token = sp.get_cached_token()
print (token)
spot = spotipy.client.Spotify(auth=token["access_token"])
# info = spot.current_user()
# print(info)
#
# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
#
# results = spot.artist_albums(taylor_uri, album_type='album')
uris = []
# for song in song_titles:
#     try:
#         results = spot.search(q = f"{song} 2025", limit=1)
#         uris.append(results["tracks"]["items"][-1]["uri"])
#     except:
#         pass

print(uris)
uris = ['spotify:track:53iuhJlwXhSER5J2IYYv1W', 'spotify:track:1CPZ5BxNNd0n0nF4Orb9JS', 'spotify:track:6qqrTXSdwiJaq8SO0X2lSe', 'spotify:track:3yWuTOYDztXjZxdE2cIRUa', 'spotify:track:1qbmS6ep2hbBRaEZFpn7BX', 'spotify:track:5BZsQlgw21vDOAjoqkNgKb', 'spotify:track:0bxPRWprUVpQK0UFcddkrA', 'spotify:track:1jgTiNob5cVyXeJ3WgX5bL', 'spotify:track:4gfrYDtaRmp6HPvN80V2ob', 'spotify:track:08M5qLQy0oUNrTMQv4xQac', 'spotify:track:03bTIHJElXZ0O0jqOQvAbY', 'spotify:track:7qjZnBKE73H4Oxkopwulqe', 'spotify:track:1I37Zz2g3hk9eWxaNkj031', 'spotify:track:2TEQvxxQabwLQMqWMg1qGu', 'spotify:track:04emojnbYkrRmv5qtJcgVP', 'spotify:track:2BwO5K8Q7EPAJSGze3AAh9', 'spotify:track:006oXsuHY7SzR8qeX40nUp', 'spotify:track:02sy7FAs8dkDNYsHp4Ul3f', 'spotify:track:0t3pcqgBjuAVBgY2oEUIlH', 'spotify:track:42VUCXerQ5qTr4Qp6PhKo4', 'spotify:track:53iuhJlwXhSER5J2IYYv1W', 'spotify:track:0xBbC1lN9GW9w2QvlnrJJg', 'spotify:track:3RXUgPNIbUgFxsDWuBQEt6', 'spotify:track:5ylJtmaWPJ33cW3En7WOu0', 'spotify:track:2x3mwb96B6TquRqMtbxUE1', 'spotify:track:2ipIPsgrgd0j2beDf4Ki70', 'spotify:track:04a44cx2PJthIbN2aLMXhl', 'spotify:track:1appZ3c336FkPvCuywfmrs', 'spotify:track:62HoDY1Km6lm47haFpUn9c', 'spotify:track:5sBDrrtLGbV64QJnEqfjer', 'spotify:track:62V2ZHslgQV98gH4AuVXnr', 'spotify:track:5Ps0z9cSf6xYIJ6lzCqTC1', 'spotify:track:4qmFC3Jz5aQ0erlk2OSi2X', 'spotify:track:1WBD2KNkYu880G7ElAituh', 'spotify:track:65DbTqJKhbwqYbZ1Okr0rc', 'spotify:track:0MHStU0muAIEMbwdnebYu2', 'spotify:track:1xOqGUkyxGQRdCvGpvWKmL', 'spotify:track:6dWilYAxP2aJbTTt0UsatK', 'spotify:track:0sLORCXBgcg2X4FTW3538D', 'spotify:track:5DxDLsW6PsLz5gkwC7Mk5S', 'spotify:track:3cZajhyr8LmtPfHZ9296tj', 'spotify:track:1vgourDwo7hFFamSxepvar', 'spotify:track:29iva9idM6rFCPUlu7Rhxl', 'spotify:track:6sGIMrtIzQjdzNndVxe397', 'spotify:track:6RFXPIMvJvOCNzBQmIUZIb', 'spotify:track:4Km9FSF9iaQiTLnFPdbPom', 'spotify:track:4JIbFfr4f2dMQQy50HHptt', 'spotify:track:4n4tC4qO2LeWQRM9Gbbtop', 'spotify:track:0aGIy8kll4HYDnNTDlf2vU', 'spotify:track:2N9miXnewVmUrgl6JSK1FI', 'spotify:track:1IHQY9xFFfgYyjOWmbCVsE', 'spotify:track:0U1nO2frLx8w2dIsfvlP1d', 'spotify:track:31Oh4pwZWjBTuRmzNtxj10', 'spotify:track:1IfGOnXoMBkiKC9xljlSfa', 'spotify:track:0WsC4ETIXyiHDMXRaPMvKe', 'spotify:track:5q9I5RmmrLC4U2mW2BnF3K', 'spotify:track:3CUjQSY81ZV6GBUcoPCBrL', 'spotify:track:6xV7Be6XEvkSnighmh2Tzj', 'spotify:track:05od2qm2MTSKCHxy1GBp5W', 'spotify:track:1zM8S2pnIclcdTmrfFnWtX', 'spotify:track:3NFs3XUduzBfvc5Bx1gmzh', 'spotify:track:0je57Uq5eTk1wrPzn9sWbl', 'spotify:track:2tQSuufhS5XHz0E8EBi55M', 'spotify:track:6WjwYL2tzzci2pvpv50rS4', 'spotify:track:7Eb9i3xmiLuY5MiY6AhzzL', 'spotify:track:3kLqlYcPuj5864tVB5LVL2', 'spotify:track:4Iu73sdCNxZXZUIyClMoPZ', 'spotify:track:5Xl87hTgoBbSnEXKNse77Q', 'spotify:track:5Opj77P3X1JeocdzqD5hb3', 'spotify:track:55lijDD6OAjLFFUHU9tcDm', 'spotify:track:2GFawZaMjG8QLxiR4OD3db', 'spotify:track:6Q3lFQgpvhA9VApFKLFZtZ', 'spotify:track:6sGIMrtIzQjdzNndVxe397', 'spotify:track:1JhU3dxmVMSRiMc2oehLcO', 'spotify:track:2uH74oFgwuk5x0DlD3EFJ1', 'spotify:track:4ZSJifET0qPf7XtPrtV6EN', 'spotify:track:0YsIYFRoxkmEvbKCwTp0Tg', 'spotify:track:2ZCDXVmOLnKUHYVpycIq5F', 'spotify:track:6vqyk3mbDBv3npTpctYoka', 'spotify:track:0MHStU0muAIEMbwdnebYu2', 'spotify:track:4SRShYMtFIGgnOU7iBicMH', 'spotify:track:212xtcXoSqbbwFAYd0zvNP', 'spotify:track:2gYTC8DsplN3RNdpdBcCOQ', 'spotify:track:00IDEhdInEtRvbMVwkBZgs', 'spotify:track:5ODQcZ7HVgSmIfmPQwUgc8', 'spotify:track:3anaHXs7z8NwLUatPxqJlE', 'spotify:track:312z6PZ8wwREck8613PkJk', 'spotify:track:17U2M7HB14yGe9QSAmbyyB', 'spotify:track:2vBhzHJZSFbrI6kddrdUmA', 'spotify:track:3rTvXpSq6fDU1PitJlmnhm', 'spotify:track:46h2irLLd7JUOecp2MnnOd', 'spotify:track:6NBZu27n3cxEk4y4c2Kxi8', 'spotify:track:2cBtsB7Pi89q9yWk59a2sX', 'spotify:track:7gKxCvTDWwV9wBhdeBbr3l', 'spotify:track:2SsY5k7UWFqgye3PUMG3Oq', 'spotify:track:0rOtJU5F5103vqBYeixFNQ', 'spotify:track:1hCgJlVQL6N2OCqs4JOibW', 'spotify:track:1BDLD4c07q0bmq2VCRsXoE', 'spotify:track:0q2zGICTMJ3ZAZX0r2RLNH', 'spotify:track:3roJNjr7zRlLyr1bTPq0AS']

response2 = spot.user_playlist_create(user=userid,name=f"{formatted_date} Billboard 100",public=False,collaborative=False,)

play_id = response2["id"]

# for track in range(1,len(uris)):
#     spot.playlist_add_items(playlist_id=play_id, items = uris[track])

spot.playlist_add_items(playlist_id=play_id, items = uris)