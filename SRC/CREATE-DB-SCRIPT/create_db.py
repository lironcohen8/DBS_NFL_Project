import os
import mysql.connector

mysql_user = "lironcohen3"
mysql_password = "lironcoh27840"
db_name = "lironcohen3"

# Dictionary for all tables we want to create with their Primary keys and foreign keys

TABLES = {}

TABLES['venues'] = (
    "CREATE TABLE `venues` ("
    "  `venue_id` INT NOT NULL,"
    "  `name` varchar(100) NOT NULL,"
    "  `capacity` INT,"
    "  `city` varchar(100),"
    "  `state` varchar(100),"
    "  PRIMARY KEY (`venue_id`)"
    ")")

TABLES['teams'] = (
    "CREATE TABLE `teams` ("
    "  `team_id` INT NOT NULL,"
    "  `team_name` varchar(100) NOT NULL,"
    "  `mascot` varchar(100),"
    "  `conference` varchar(100),"
    "  `venue_id` INT,"
    "  `twitter` varchar(100),"
    "  PRIMARY KEY (`team_id`),"
    "  FOREIGN KEY (`venue_id`) REFERENCES venues(`venue_id`)" 
    ")")

TABLES['games'] = (
    "CREATE TABLE `games` ("
    "  `game_id` INT NOT NULL,"
    "  `season` INT,"
    "  `week` INT,"
    "  `venue_id` INT,"
    "  `home_id` INT,"
    "  `home_points` INT,"
    "  `home_post_win_prob` FLOAT,"
    "  `away_id` INT,"
    "  `away_points` INT,"
    "  `away_post_win_prob` FLOAT,"
    "  PRIMARY KEY (`game_id`),"
    "  FOREIGN KEY (`venue_id`) REFERENCES venues(`venue_id`),"
    "  FOREIGN KEY (`home_id`) REFERENCES teams(`team_id`),"
    "  FOREIGN KEY (`away_id`) REFERENCES teams(`team_id`)"
    ")")

TABLES['players'] = (
    "CREATE TABLE `players` ("
    "  `player_id` INT NOT NULL,"
    "  `season` INT,"
    "  `name` varchar(100) NOT NULL,"
    "  `position` varchar(100),"
    "  `team` varchar(100),"
    "  `overall` FLOAT,"
    "  `pass` FLOAT,"
    "  `rush` FLOAT,"
    "  `first_down` FLOAT,"
    "  `second_down` FLOAT,"
    "  `third_down` FLOAT,"
    "  `standard_downs` FLOAT,"
    "  `passing_downs` FLOAT,"
    "  PRIMARY KEY (`player_id`)"
    ")")

TABLES['stats'] = (
    "CREATE TABLE `stats` ("
    "  `team` varchar(100) NOT NULL,"
    "  `season` INT,"
    "  `conference` varchar(100),"
    "  `stat_name` varchar(100) NOT NULL,"
    "  `stat_value` INT,"
    "  PRIMARY KEY (`team`, `stat_name`)"
    ")")

TABLES['draft_positions'] = (
    "CREATE TABLE `draft_positions` ("
    "  `position_name` varchar(100) NOT NULL,"
    "  `abbreviation` varchar(100),"
    "  PRIMARY KEY (`position_name`)"
    ")")

TABLES['draft_picks'] = (
    "CREATE TABLE `draft_picks` ("
    "  `college_athlete_id` INT NOT NULL,"
    "  `nfl_athlete_id` INT,"
    "  `college_id` INT,"
    "  `college_team` varchar(100),"
    "  `nfl_team` varchar(100),"
    "  `name` varchar(100),"
    "  `position` varchar(100),"
    "  `height` INT,"
    "  `weight` INT,"
    "  `overall` INT,"
    "  `round` INT,"
    "  `pick` INT,"
    "  PRIMARY KEY (`college_athlete_id`),"
    "  FOREIGN KEY (`position`) REFERENCES draft_positions(`position_name`),"
    "  FOREIGN KEY (`college_id`) REFERENCES teams(`team_id`)" 
    ")")

TABLES['draft_teams'] = (
    "CREATE TABLE `draft_teams` ("
    "  `display_name` varchar(100) NOT NULL,"
    "  `nickname` varchar(100),"
    "  `location` varchar(100),"
    "  PRIMARY KEY (`display_name`)"
    ")")

INDEXES = {}
INDEXES['games_home_id'] = (
    "CREATE INDEX home_id_ind ON games(`home_id`)")

INDEXES['game_away_id'] = (
    "CREATE INDEX away_id_ind ON games(`away_id`)")

INDEXES['teams'] = (
    "CREATE INDEX team_name_ind ON teams(`team_name`)")

INDEXES['players_team'] = (
    "CREATE INDEX team_ind ON players(`team`)")

INDEXES['players_position'] = (
    "CREATE INDEX position_ind ON players(`position`)")

INDEXES['stats_name'] = (
    "CREATE INDEX stat_name_ind ON stats(`stat_name`)")

INDEXES['stats_team'] = (
    "CREATE INDEX team_ind ON stats(`team`)")

INDEXES['venues'] = (
    "CREATE INDEX capacity_ind ON venues(`capacity`)")

INDEXES['draft_picks'] = (
    "CREATE INDEX college_id_ind ON draft_picks(`college_id`)")

INDEXES['draft_teams'] = (
    "CREATE INDEX location_ind ON draft_teams(`location`)")


# Creating connection to the DB and defines its tables schemas
class DBCreator:

    # Initialize the connection to the DB
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3305,
            user=mysql_user,
            password=mysql_password,
            database=db_name
        )

    # Foreach table constructed above -> create table
    def create_all_tables(self):
        cursor = self.conn.cursor()
        for table_name in TABLES.keys():
            try:
                cursor.execute(TABLES[table_name])
                self.conn.commit()
            except mysql.connector.Error as err:
                self.conn.rollback()
                # rollback in case of failure will make our creation atomic

    def create_all_indexes(self):
        cursor = self.conn.cursor()
        for index_name in INDEXES.keys():
            try:
                cursor.execute(INDEXES[index_name])
                self.conn.commit()
            except mysql.connector.Error as err:
                self.conn.rollback()
                # rollback in case of failure will make our creation atomic

    # Close connection to db
    def close_connection(self):
        self.conn.close()


if __name__ == '__main__':
    # un-comment next line for connecting to tau servers 
    # os.system("ssh -L 3305:mysqlsrv1.cs.tau.ac.il:3306 lironcohen3@nova.cs.tau.ac.il")

    db_creator = DBCreator()
    db_creator.create_all_tables()
    db_creator.create_all_indexes()
    db_creator.close_connection()
