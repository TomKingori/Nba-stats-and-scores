from requests import get
from pprint import pprint

from sympy import li

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        pprint(game.keys())
        break

get_scoreboard()