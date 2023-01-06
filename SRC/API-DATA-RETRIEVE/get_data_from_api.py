import json
import requests

college_football_key = "wy5y2yEYzKbBI8kaIIVqyqzVbBpfTk+kakI1OKiogGfB894/GuGqXbgVO5l8bRVH"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer wy5y2yEYzKbBI8kaIIVqyqzVbBpfTk+kakI1OKiogGfB894/GuGqXbgVO5l8bRVH"
}


# Getting data from the API
class APIDataGetter:

    @staticmethod
    def get_games():  # Number of records - 3668
        res = requests.get(f"https://api.collegefootballdata.com/games?year=2022&seasonType=regular", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_teams():  # Number of records - 1790
        res = requests.get(f"https://api.collegefootballdata.com/teams", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_players():  # Number of records - 2616
        res = requests.get(f"https://api.collegefootballdata.com/player/usage?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_stats():  # Number of records - 4192
        res = requests.get(f"https://api.collegefootballdata.com/stats/season?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_venues():  # Number of records - 804
        res = requests.get(f"https://api.collegefootballdata.com/venues", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_positions():  # Number of records - 28
        res = requests.get(f"https://api.collegefootballdata.com/draft/positions", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_picks():  # Number of records - 262
        res = requests.get(f"https://api.collegefootballdata.com/draft/picks?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_teams():  # Number of records - 32
        res = requests.get(f"https://api.collegefootballdata.com/draft/teams", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None
