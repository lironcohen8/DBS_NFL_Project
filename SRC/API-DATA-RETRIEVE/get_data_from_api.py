import json
import requests

college_football_key = "wy5y2yEYzKbBI8kaIIVqyqzVbBpfTk+kakI1OKiogGfB894/GuGqXbgVO5l8bRVH"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer wy5y2yEYzKbBI8kaIIVqyqzVbBpfTk+kakI1OKiogGfB894/GuGqXbgVO5l8bRVH"
}


class APIDataGetter:

    @staticmethod
    def get_games():  # 3667
        res = requests.get(f"https://api.collegefootballdata.com/games?year=2022&seasonType=regular", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_teams():  # 1790
        res = requests.get(f"https://api.collegefootballdata.com/teams", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_players():  # 2616
        res = requests.get(f"https://api.collegefootballdata.com/player/usage?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_stats():  # 4192
        res = requests.get(f"https://api.collegefootballdata.com/stats/season?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_venues():  # 804
        res = requests.get(f"https://api.collegefootballdata.com/venues", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_positions():  # 28
        res = requests.get(f"https://api.collegefootballdata.com/draft/positions", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_picks():  # 262
        res = requests.get(f"https://api.collegefootballdata.com/draft/picks?year=2022", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None

    @staticmethod
    def get_draft_teams():  # 32
        res = requests.get(f"https://api.collegefootballdata.com/draft/teams", headers=headers)
        if res.status_code == 200:
            data = json.loads(res.content)
            return data
        return None