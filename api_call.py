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


def dictionary_filter(dict, column, value):
    desired_value = [d for d in dict if d[column] in {value}]
    return desired_value


search_query = "game"
search_results = search_board_games(search_query)


video_games = dictionary_filter(search_results, "type", "videogame")
board_games = dictionary_filter(search_results, "type", "boardgame")
