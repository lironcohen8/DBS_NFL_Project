import json
import requests

sportsdata_io_api_key = "33f96f364f914387ab00b15698717161"


def get_players():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/Players?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_referees():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/Referees?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_stadiums():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/Stadiums?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_standings_2023():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/Standings/2023?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_all_teams():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/AllTeams?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_injured_players():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/projections/json/InjuredPlayers?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_players_stats_2023():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2023?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def get_games_2023():
    res = requests.get(f"https://api.sportsdata.io/v3/nba/scores/json/Games/2023?key={sportsdata_io_api_key}")
    if res.status_code == 200:
        data = json.loads(res.content)
    return None


def main():
    get_players()
    get_referees()
    get_stadiums()
    get_standings_2023()
    get_all_teams()
    get_injured_players()
    get_players_stats_2023()
    get_games_2023()


if __name__ == "__main__":
    main()
