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
                game_id = int(game['id']) if game['id'] is not None else None
                season = int(game['season']) if game['season'] is not None else None
                week = int(game['week']) if game['week'] is not None else None
                venue_id = int(game['venue_id']) if game['venue_id'] is not None else None
                home_id = int(game['home_id']) if game['home_id'] is not None else None
                home_points = int(game['home_points']) if game['home_points'] is not None else None
                home_post_win_prob = float(game['home_post_win_prob']) if game['home_post_win_prob'] is not None else None
                away_id = int(game['away_id']) if game['away_id'] is not None else None
                away_points = int(game['away_points']) if game['away_points'] is not None else None
                away_post_win_prob = float(game['away_post_win_prob']) if game['away_post_win_prob'] is not None else None

                games_query = """INSERT INTO games(game_id,season,week,venue_id,home_id,home_points,home_post_win_prob,away_id,away_points,away_post_win_prob)
                                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(games_query, (game_id, season, week, venue_id, home_id, home_points, home_post_win_prob, away_id, away_points, away_post_win_prob))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_teams_data(self):
        teams = APIDataGetter.get_teams()

        for team in teams:
            team_id = team['id']
            if team_id:
                team_id = int(team['id']) if team['id'] is not None else None
                team_name = f"{team['school']}" if team['school'] is not None else None
                mascot = f"{team['mascot']}" if team['mascot'] is not None else None
                conference = f"{team['conference']}" if team['conference'] is not None else None
                venue_id = int(team['location']['venue_id']) if team['location']['venue_id'] is not None else None
                twitter = f"{team['twitter']}" if team['twitter'] is not None else None

                teams_query = """INSERT INTO teams(team_id,team_name,mascot,conference,venue_id,twitter)
                                 VALUES(%s,%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(teams_query, (team_id, team_name, mascot, conference, venue_id, twitter))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_players_data(self):
        players = APIDataGetter.get_players()

        for player in players:
            player_id = player['id']
            if player_id:
                player_id = int(player['id']) if player['id'] is not None else None
                season = int(player['season']) if player['season'] is not None else None
                name = f"{player['name']}" if player['name'] is not None else None
                position = f"{player['position']}" if player['position'] is not None else None
                team = f"{player['team']}" if player['team'] is not None else None
                overall = float(player['usage']['overall']) if player['usage']['overall'] is not None else None
                pass_ = float(player['usage']['pass']) if player['usage']['pass'] is not None else None
                rush = float(player['usage']['rush']) if player['usage']['rush'] is not None else None
                first_down = float(player['usage']['firstDown']) if player['usage']['firstDown'] is not None else None
                second_down = float(player['usage']['secondDown']) if player['usage']['secondDown'] is not None else None
                third_down = float(player['usage']['thirdDown']) if player['usage']['thirdDown'] is not None else None
                standard_downs = float(player['usage']['standardDowns']) if player['usage']['standardDowns'] is not None else None
                passing_downs = float(player['usage']['passingDowns']) if player['usage']['passingDowns'] is not None else None

                players_query = """INSERT INTO players(player_id,season,name,position,team,overall,pass,rush,first_down,second_down,third_down,standard_downs,passing_downs) 
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(players_query, (player_id, season, name, position, team, overall, pass_, rush, first_down, second_down, third_down, standard_downs, passing_downs))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_stats_data(self):
        stats = APIDataGetter.get_stats()

        for stat in stats:
            team = stat['team']
            if team:
                team = f"{stat['team']}" if stat['team'] is not None else None
                season = int(stat['season']) if stat['season'] is not None else None
                conference = f"{stat['team']}" if stat['team'] is not None else None
                stat_name = f"{stat['statName']}" if stat['statName'] is not None else None
                stat_value = int(stat['statValue']) if stat['statValue'] is not None else None

                stats_query = """INSERT INTO stats(team,season,conference,stat_name,stat_value) 
                                 VALUES(%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(stats_query, (team, season, conference, stat_name, stat_value))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_venues_data(self):
        venues = APIDataGetter.get_venues()

        for venue in venues:
            venue_id = venue['id']
            if venue_id:
                venue_id = int(venue['id']) if venue['id'] is not None else None
                name = f"{venue['name']}" if venue['name'] is not None else None
                capacity = int(venue['capacity']) if venue['capacity'] is not None else None
                city = f"{venue['city']}" if venue['city'] is not None else None
                state = f"{venue['state']}" if venue['state'] is not None else None

                venues_query = """INSERT INTO venues(venue_id,name,capacity,city,state)
                                  VALUES(%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(venues_query, (venue_id, name, capacity, city, state))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_draft_positions_data(self):
        draft_positions = APIDataGetter.get_draft_positions()

        for position in draft_positions:
            position_name = position['name']
            if position_name:
                position_name = f"{position['name']}" if position['name'] is not None else None
                abbreviation = f"{position['abbreviation']}" if position['abbreviation'] is not None else None

                draft_positions_query = """INSERT INTO draft_positions(position_name, abbreviation)
                                           VALUES (%s, %s)"""

                try:
                    self.cursor.execute(draft_positions_query, (position_name, abbreviation))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_draft_picks_data(self):
        draft_picks = APIDataGetter.get_draft_picks()

        for draft_pick in draft_picks:
            college_athlete_id = draft_pick['collegeAthleteId']
            if college_athlete_id:
                college_athlete_id = int(draft_pick['collegeAthleteId']) if draft_pick['collegeAthleteId'] is not None else None
                nfl_athlete_id = int(draft_pick['nflAthleteId']) if draft_pick['nflAthleteId'] is not None else None
                college_id = int(draft_pick['collegeId']) if draft_pick['collegeId'] is not None else None
                college_team = f"{draft_pick['collegeTeam']}" if draft_pick['collegeTeam'] is not None else None
                nfl_team = f"{draft_pick['nflTeam']}" if draft_pick['nflTeam'] is not None else None
                name = f"{draft_pick['name']}" if draft_pick['name'] is not None else None
                position = f"{draft_pick['position']}" if draft_pick['position'] is not None else None
                height = int(draft_pick['height']) if draft_pick['height'] is not None else None
                weight = int(draft_pick['weight']) if draft_pick['weight'] is not None else None
                overall = int(draft_pick['overall']) if draft_pick['overall'] is not None else None
                round_ = int(draft_pick['round']) if draft_pick['round'] is not None else None
                pick = int(draft_pick['pick']) if draft_pick['pick'] is not None else None

                draft_picks_query = """INSERT INTO draft_picks(college_athlete_id,nfl_athlete_id,college_id,college_team,nfl_team,name,position,height,weight,overall,round,pick)
                                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                try:
                    self.cursor.execute(draft_picks_query, (college_athlete_id, nfl_athlete_id, college_id, college_team, nfl_team, name, position, height, weight, overall, round_, pick))
                    self.conn.commit()
                except mysql.connector.Error as err:
                    if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                        self.conn.rollback()

    def insert_draft_teams_data(self):
        draft_teams = APIDataGetter.get_draft_teams()

        for draft_team in draft_teams:
            display_name = draft_team['displayName']
            if display_name:
                display_name = f"{draft_team['displayName']}" if draft_team['displayName'] is not None else None
                nickname = f"{draft_team['nickname']}" if draft_team['nickname'] is not None else None
                location = f"{draft_team['location']}" if draft_team['location'] is not None else None

            draft_teams_query = """INSERT INTO draft_teams(display_name,nickname,location) 
                                   VALUES(%s, %s, %s)"""

            try:
                self.cursor.execute(draft_teams_query, (display_name, nickname, location))
                self.conn.commit()
            except mysql.connector.Error as err:
                if err.errno != 1062 and err.errno != 1216:  # Duplicate entry for primary key or foreign key constraints
                    self.conn.rollback()

    def close_conn(self):
        self.conn.close()

    # fill all tables with data from the API
    def fill_all_tables(self):
        self.insert_venues_data()
        self.insert_teams_data()
        self.insert_games_data()
        self.insert_players_data()
        self.insert_stats_data()
        self.insert_draft_positions_data()
        self.insert_draft_picks_data()
        self.insert_draft_teams_data()


if __name__ == '__main__':
    data_inserter = APIDataInserter()
    data_inserter.fill_all_tables()
    data_inserter.close_conn()
