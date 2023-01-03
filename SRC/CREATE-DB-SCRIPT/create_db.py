import mysql.connector

mysql_user = "lironcohen3"
mysql_password = "lironcoh27840"
db_name = "lironcohen3"

# Dictionary for all tables we want to create with their Primary keys and foreign keys

TABLES = {}
TABLES['games'] = (
    "CREATE TABLE `games` ("
    "  `game_id` INT NOT NULL,"
    "  `season` INT,"
    "  `week` INT,"
    "  `venue_id` INT,"
    "  `venue` varchar(100),"
    "  `home_id` INT,"
    "  `home_team` varchar(100),"
    "  `home_conference` varchar(100),"
    "  `home_points` INT,"
    "  `home_post_win_prob` FLOAT,"
    "  `away_id` INT,"
    "  `away_team` varchar(100),"
    "  `away_conference` varchar(100),"
    "  `away_points` INT,"
    "  `away_post_win_prob` FLOAT,"
    "  PRIMARY KEY (`game_id`)"
    ")")

TABLES['teams'] = (
    "CREATE TABLE `teams` ("
    "  `team_id` INT NOT NULL,"
    "  `school` varchar(100) NOT NULL,"
    "  `mascot` varchar(100),"
    "  `conference` varchar(100),"
    "  `venue_id` INT,"
    "  `twitter` varchar(100),"
    "  PRIMARY KEY (`team_id`)"
    ")")

TABLES['players'] = (
    "CREATE TABLE `players` ("
    "  `player_id` INT NOT NULL,"
    "  `season` INT,"
    "  `name` varchar(100) NOT NULL,"
    "  `position` varchar(100),"
    "  `team` varchar(100),"
    "  `conference` varchar(100),"
    "  `overall` FLOAT,"
    "  `pass` FLOAT,"
    "  `rush` FLOAT,"
    "  `firstDown` FLOAT,"
    "  `secondDown` FLOAT,"
    "  `thirdDown` FLOAT,"
    "  `standardDowns` FLOAT,"
    "  `passingDowns` FLOAT,"
    "  PRIMARY KEY (`player_id`)"
    ")")

TABLES['stats'] = (
    "CREATE TABLE `stats` ("
    "  `team` varchar(100) NOT NULL,"
    "  `season` INT,"
    "  `conference` varchar(100),"
    "  `statName` varchar(100),"
    "  `statValue` varchar(100),"
    "  PRIMARY KEY (`team`)"
    ")")

TABLES['venues'] = (
    "CREATE TABLE `venues` ("
    "  `venue_id` INT NOT NULL,"
    "  `name` varchar(100) NOT NULL,"
    "  `capacity` INT,"
    "  `city` varchar(100),"
    "  `state` varchar(100),"
    "  PRIMARY KEY (`venue_id`)"
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
    "  `college_conference` varchar(100),"
    "  `nfl_team` varchar(100),"
    "  `name` varchar(100),"
    "  `position` varchar(100),"
    "  `height` INT,"
    "  `weight` INT,"
    "  `overall` INT,"
    "  `round` INT,"
    "  `pick` INT,"
    "  PRIMARY KEY (`college_athlete_id`)"
    ")")

TABLES['draft_teams'] = (
    "CREATE TABLE `draft_teams` ("
    "  `display_name` varchar(100) NOT NULL,"
    "  `nickname` varchar(100),"
    "  `location` varchar(100),"
    "  PRIMARY KEY (`display_name`)"
    ")")


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

    # Close connection to db
    def close_connection(self):
        self.conn.close()


if __name__ == '__main__':
    # un-comment next line for connecting to tau servers 
    # os.system("ssh -L 3305:mysqlsrv1.cs.tau.ac.il:3306 lironcohen3@nova.cs.tau.ac.il")

    db_creator = DBCreator()
    db_creator.create_all_tables()
    db_creator.close_connection()
