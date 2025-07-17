import requests
from bs4 import BeautifulSoup

url = "https://jikan.moe"  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

songs = []

for item in soup.select("li.song"):
    artist = item.select_one(".artist").text
    title = item.select_one(".title").text
    songs.append(f"{artist} - {title}")

with open("songs.txt", "w", encoding="utf-8") as f:
    for song in songs:
        f.write(song + "\n")