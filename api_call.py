import requests
from xml.etree import ElementTree as ET


def search_board_games(query):
    url = f"https://www.boardgamegeek.com/xmlapi2/search?query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        games = []

        for item in root.findall("item"):
            game = {
                "name": item.find("name").get("value"),
                "id": item.get("id"),
                "type": item.get("type"),
                "yearpublished": item.find("yearpublished").get("value")
                if item.find("yearpublished") is not None
                else "Not Available",
            }
            games.append(game)

        return games


search_query = ""
search_results = search_board_games(search_query)
