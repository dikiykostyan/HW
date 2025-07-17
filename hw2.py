import requests
import json

url = "https://api.jikan.moe/v4/top/anime"
response = requests.get(url)
data = response.json()

popular = []
for anime in data["data"]:
    popular.append({
        "title": anime["title"],
        "score": anime.get("score", "N/A")
    })

with open("popular_anime.json", "w", encoding="utf-8") as f:
    json.dump(popular, f, ensure_ascii=False, indent=2)