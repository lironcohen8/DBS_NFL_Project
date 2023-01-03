import mysql.connector
from get_data_from_api import APIDataGetter

mysql_user = "lironcohen3"
mysql_password = "lironcoh27840"
db_name = "lironcohen3"


# Creating connection to the DB and inserts the data from the API into the tables
class APIDataInserter:

    # Initialize the connection to the DB
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3305,
            user=mysql_user,
            password=mysql_password,
            database=db_name
        )
        self.cursor = self.conn.cursor()

    def insert_games_data(self):
        games = APIDataGetter.get_games()

        for game in games:
            game_id = game['id']
            if game_id:
                game_id = game['id']
                season = game['season']
                week = game['week']
                venue_id = game['venue_id']
                venue = game['venue']
                home_id = game['home_id']
                home_team = game['home_team']
                home_conference = game['home_conference']
                home_points = game['home_points']
                home_post_win_prob = game['home_post_win_prob']
                away_id = game['home_id']
                away_team = game['home_team']
                away_conference = game['home_conference']
                away_points = game['home_points']
                away_post_win_prob = game['home_post_win_prob']

                games_query = f"""INSERT INTO games(game_id,season,week,venue_id,venue,home_id,home_team,home_conference,home_points,home_post_win_prob,away_id,away_team,away_conference,away_points,away_post_win_prob) VALUES({game_id},{season},{week},{venue_id},{venue},{home_id},{home_team},{home_conference},{home_points},{home_post_win_prob},{away_id},{away_team},{away_conference},{away_points},{away_post_win_prob})"""

                try:
                    self.cursor.execute(games_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_teams_data(self):
        teams = APIDataGetter.get_teams()

        for team in teams:
            team_id = team['id']
            if team_id:
                team_id = team['id']
                school = team['school']
                mascot = team['mascot']
                conference = team['conference']
                venue_id = team['location']['venue_id']
                twitter = team['twitter']

                teams_query = f"""INSERT INTO teams(team_id,school,mascot,conference,venue_id,twitter) VALUES({team_id},{school},{mascot},{conference},{venue_id},{twitter}")"""

                try:
                    self.cursor.execute(teams_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_players_data(self):
        players = APIDataGetter.get_players()

        for player in players:
            player_id = player['id']
            if player_id:
                player_id = player['id']
                season = player['season']
                name = player['name']
                position = player['position']
                team = player['team']
                conference = player['conference']
                overall = player['usage']['overall']
                pass_ = player['usage']['pass']
                rush = player['usage']['rush']
                firstDown = player['usage']['firstDown']
                secondDown = player['usage']['secondDown']
                thirdDown = player['usage']['thirdDown']
                standardDowns = player['usage']['standardDowns']
                passingDowns = player['usage']['passingDowns']

                players_query = f"""INSERT INTO players(player_id,season,name,position,team,conference,overall,pass,rush,firstDown,secondDown,thirdDown,standardDowns,passingDowns) VALUES({player_id},{season},{name},{position},{team},{conference},{overall},{pass_},{rush},{firstDown},{secondDown},{thirdDown},{standardDowns},{passingDowns}")"""

                try:
                    self.cursor.execute(players_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_stats_data(self):
        stats = APIDataGetter.get_stats()

        for stat in stats:
            team = stat['team']
            if team:
                team = stat['team']
                season = stat['season']
                conference = stat['conference']
                statName = stat['statName']
                statValue = stat['statValue']

                stats_query = f"""INSERT INTO stats(team,season,conference,statName,statValue) VALUES({team},{season},{conference},{statName},{statValue}")"""

                try:
                    self.cursor.execute(stats_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_venues_data(self):
        venues = APIDataGetter.get_venues()

        for venue in venues:
            venue_id = venue['id']
            if venue_id:
                venue_id = venue['id']
                name = venue['name']
                capacity = venue['capacity']
                city = venue['city']
                state = venue['state']

                venues_query = f"""INSERT INTO venues(venue_id,name,capacity,city,state) VALUES({venue_id},{name},{capacity},{city},{state}")"""

                try:
                    self.cursor.execute(venues_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_draft_positions_data(self):
        draft_positions = APIDataGetter.get_draft_positions()

        for position in draft_positions:
            position_name = position['name']
            if position_name:
                position_name = position['name']
                abbreviation = position['abbreviation']

                draft_positions_query = f"""INSERT INTO draft_positions(position_name,abbreviation) VALUES({position_name},{abbreviation}")"""

                try:
                    self.cursor.execute(draft_positions_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_draft_picks_data(self):
        draft_picks = APIDataGetter.get_draft_picks()

        for draft_pick in draft_picks:
            college_athlete_id = draft_pick['collegeAthleteId']
            if college_athlete_id:
                college_athlete_id = draft_pick['collegeAthleteId']
                nfl_athlete_id = draft_pick['nflAtheleteId']
                college_id = draft_pick['collegeId']
                college_team = draft_pick['collegeTeam']
                college_conference = draft_pick['collegeConference']
                nfl_team = draft_pick['nflTeam']
                name = draft_pick['name']
                position = draft_pick['position']
                height = draft_pick['height']
                weight = draft_pick['weight']
                overall = draft_pick['overall']
                round = draft_pick['round']
                pick = draft_pick['pick']

                draft_picks_query = f"""INSERT INTO draft_picks(college_athlete_id,nfl_athlete_id,college_id,college_team,college_conference,nfl_team,name,position,height,weight,overall,round,pick) VALUES({college_athlete_id},{nfl_athlete_id},{college_id},{college_team},{college_conference},{nfl_team},{name},{position},{height},{weight},{overall},{round},{pick}")"""

                try:
                    self.cursor.execute(draft_picks_query)
                    self.conn.commit()
                except mysql.connector.Error:
                    self.conn.rollback()

    def insert_draft_teams_data(self):
        draft_teams = APIDataGetter.get_draft_teams()

        for draft_team in draft_teams:
            display_name = draft_team['displayName']
            if display_name:
                display_name = draft_team['displayName']
                nickname = draft_team['nickname']
                location = draft_team['location']

            draft_teams_query = f"""INSERT INTO draft_teams(display_name,nickname,location) VALUES({display_name},{nickname},{location}")"""

            try:
                self.cursor.execute(draft_teams_query)
                self.conn.commit()
            except mysql.connector.Error:
                self.conn.rollback()
