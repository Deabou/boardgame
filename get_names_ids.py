import requests
import json
from xml.etree import ElementTree as ET


def search_board_games(query):
    url = f"https://www.boardgamegeek.com/xmlapi2/search?query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.content
    else:
        print(
            f"Failed to fetch search results for query '{query}'. Status code: {response.status_code}"
        )
        return None


search_board_games("board game")
