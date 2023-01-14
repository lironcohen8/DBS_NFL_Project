import os
import mysql.connector

mysql_user = "lironcohen3"
mysql_password = "lironcoh27840"
db_name = "lironcohen3"


class DBQuery:
    def __init__(self):

        self.conn = mysql.connector.connect(
            host='localhost',
            port=3305,
            user=mysql_user,
            password=mysql_password,
            database=db_name
        )
        self.cursor = self.conn.cursor()

    # query 1
    def m(self):

        query = """SELECT T1.team_name AS home_team, T2.team_name as away_team, G.season, G.week, G.away_points, G.home_points, G.away_post_win_prob AS prob, V.name as venue_name
                    FROM
                        lironcohen3.games as G,
                        lironcohen3.venues as V,
                        lironcohen3.teams as T1,
                        lironcohen3.teams as T2
                    WHERE
                        (G.venue_id = V.venue_id AND G.home_id = T1.team_id AND G.away_id = T2.team_id)
                        AND (G.home_post_win_prob > G.away_post_win_prob AND G.home_points < G.away_points)
                        AND (G.away_points - G.home_points > 10  AND G.away_post_win_prob < 0.4) 
                UNION 
                SELECT T1.team_name AS home_team, T2.team_name as away_team, G.season, G.week, G.away_points, G.home_points, G.away_post_win_prob AS prob, V.name as venue_name
                    FROM
                        lironcohen3.games as G,
                        lironcohen3.venues as V,
                        lironcohen3.teams as T1,
                        lironcohen3.teams as T2
                    WHERE
                        (G.venue_id = V.venue_id AND G.home_id = T1.team_id AND G.away_id = T2.team_id)
                        AND (G.home_post_win_prob < G.away_post_win_prob AND G.home_points > G.away_points)
                        AND (G.home_points - G.away_points > 10  AND G.home_post_win_prob < 0.4)
                ORDER BY prob"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    # query 2
    def get_top_position_players_stats(self, input_position_abb):

        query = f"""SELECT P.player_id, P.name, P.position, T.team_name, 
                        SUM(CASE WHEN G.home_points > G.away_points THEN 1 ELSE 0 END) AS wins,
                        SUM(CASE WHEN G.home_points = G.away_points THEN 1 ELSE 0 END) AS ties,
                        SUM(CASE WHEN G.home_points < G.away_points THEN 1 ELSE 0 END) AS losses,
                        AVG(P.first_down) AS avg_first_down,
                        AVG(P.second_down) AS avg_second_down, 
                        AVG(P.third_down) AS avg_third_down
                   FROM
                        lironcohen3.players AS P
                   LEFT JOIN lironcohen3.teams AS T
                        ON P.team = T.team_name
                   LEFT JOIN lironcohen3.games AS G
                        ON (G.home_id = T.team_id OR G.away_id = T.team_id)
                   WHERE 
                        P.position = "{input_position_abb}"
                   GROUP BY P.player_id
                   ORDER BY first_down DESC
                   LIMIT 50"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    # query 3
    def get_team_stats_better_than_average(self, input_team_name):

        query = f"""SELECT s1.team, s1.stat_name, s1.stat_value
                    FROM lironcohen3.stats AS s1
                    WHERE
                        s1.team = "{input_team_name}"
                        AND s1.stat_value >= (SELECT AVG(s2.stat_value) AS average_value
                                            FROM lironcohen3.stats AS s2
                                            WHERE s1.stat_name = s2.stat_name
                                            GROUP BY s2.stat_name)"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    # query 4
    def get_max_capacity_venue_per_state(self):

        query = f"""SELECT v1.state, v1.name, v1.capacity
                    FROM lironcohen3.venues AS v1
                    WHERE v1.state <> ""
                        AND v1.capacity >= ALL (SELECT v2.capacity
                                                FROM lironcohen3.venues AS v2
                                                WHERE v2.state = v1.state)"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    # query 5
    def get_min_max_weights_heights_per_draft_position(self):

        query = f"""# convertion rate from pound to kg is 0.0254
                    # convertion rate from inch to meter is 0.4535

                    SELECT Dpos.position_name, Dpos.abbreviation, 
                        MIN(Dpick.height) * 0.0254 AS min_height_meter, 
                        MAX(Dpick.height) * 0.0254 AS max_height_meter, 
                        MIN(Dpick.weight) * 0.4535 AS min_weight, 
                        MAX(Dpick.weight) * 0.4535 AS max_weight
                    FROM
                        lironcohen3.draft_picks AS Dpick,
                        lironcohen3.draft_teams as DT,
                        lironcohen3.draft_positions as Dpos
                    WHERE 
                        DT.location = Dpick.nfl_team
                        AND Dpos.position_name = Dpick.position
                    GROUP BY Dpos.position_name"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    # query 6
    def get_most_picked_college_teams_in_draft(self):

        query = f"""SELECT T.team_name, T.conference, T.mascot, T.twitter, V.name AS venue_name, SUM(DP.overall) AS sum_overall_draft
                    FROM
                        lironcohen3.draft_picks AS DP,
                        lironcohen3.teams AS T,
                        lironcohen3.venues AS V
                    WHERE
                        T.team_id = DP.college_id
                        AND T.venue_id = V.venue_id
                    GROUP BY T.team_name, T.team_id
                    ORDER BY sum_overall_draft DESC
                    LIMIT 10"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except mysql.connector.Error as err:
            rows = None
        return rows

    def close_conn(self):
        self.conn.close()


if __name__ == '__main__':
    # os.system("ssh -L 3305:mysqlsrv1.cs.tau.ac.il:3306 lironcohen3@nova.cs.tau.ac.il")

    db_query = DBQuery()
    db_query.get_teams_that_won_against_odds()
    db_query.get_top_position_players_stats("QB")
    db_query.get_team_stats_better_than_average("Miami")
    db_query.get_max_capacity_venue_per_state()
    db_query.get_min_max_weights_heights_per_draft_position()
    db_query.get_most_picked_college_teams_in_draft()
    db_query.close_conn()
