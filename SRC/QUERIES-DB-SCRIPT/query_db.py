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
    def get_most_popular_languages(self):

        query = """SELECT AVG(films.popularity) as average_popularity, languages.name
                FROM films JOIN languages ON films.language_code = languages.language_code
                WHERE films.popularity > (SELECT AVG(films.popularity)
                                        FROM films	
                                        ) 
                GROUP BY languages.name
                ORDER BY average_popularity DESC"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    # query 2
    def get_avg_revenue_per_country(self):

        query = """SELECT countries.name, AVG(films.revenue) as average_revenue
                FROM films JOIN countries ON films.country_code = countries.country_code
                WHERE films.revenue>0
                GROUP BY countries.country_code
                ORDER BY average_revenue DESC"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    # query 3
    def get_profitable_genre_by_country(self, input_country):

        query = f"""SELECT genres.name, AVG(films.revenue) as average_revenue
                FROM films JOIN film_genre ON films.tmdb_id = film_genre.film_id
                    JOIN genres ON film_genre.genre_id = genres.genre_id
                    JOIN countries ON films.country_code = countries.country_code
                WHERE films.revenue>0 and countries.name = "{input_country}"
                GROUP BY genres.name
                ORDER BY average_revenue DESC"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    # query 4
    def get_popular_actors_by_genre(self, input_genre):

        query = f"""SELECT genres.name, actors.name, FLOOR(AVG(actors.popularity)) as average_popularity, count(*) num_of_movies
                    FROM films JOIN film_genre ON films.tmdb_id = film_genre.film_id
                    JOIN genres ON film_genre.genre_id = genres.genre_id
                    JOIN film_actors ON films.tmdb_id = film_actors.film_id
                    JOIN actors ON film_actors.actor_id = actors.actor_id
                    WHERE genres.name = "{input_genre}"
                    GROUP BY actors.name
                    ORDER BY average_popularity DESC, num_of_movies DESC"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    # query 5
    def get_roi_by_country_and_genre(self):

        query = f"""SELECT countries.name, genres.name, ROUND((AVG(budget)/AVG(revenue)),2) as roi
                    FROM films JOIN film_genre ON films.tmdb_id = film_genre.film_id
                    JOIN genres ON film_genre.genre_id = genres.genre_id
                    JOIN countries ON films.country_code = countries.country_code
                    WHERE films.revenue>0
                    GROUP BY countries.name, genres.name
                    ORDER BY roi DESC"""

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    # query 6
    def get_roi_of_movie_compared_to_avg_roi(self):

        query = f"""SELECT nest.film_title, nest.country_name, ROUND((nest.film_revenue/nest.film_budget),2) as film_roi, 
                ROUND((nest.average_revenue_per_country/nest.average_budget_per_country),2) as average_country_roi
                FROM(SELECT films.title as film_title, countries.name as country_name, 
                films.popularity as film_popularity, films.budget as film_budget, films.revenue as film_revenue,
                AVG(revenue) OVER(PARTITION BY countries.name) as average_revenue_per_country,
                AVG(budget) OVER(PARTITION BY countries.name) as average_budget_per_country
                FROM films JOIN countries ON films.country_code = countries.country_code
                ) as nest
                WHERE nest.average_revenue_per_country > 0 and nest.average_budget_per_country>0 and nest.film_revenue>0 and nest.film_budget>0
                ORDER BY nest.film_popularity DESC
                """

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
        except:
            rows = None
        return rows

    def close_conn(self):
        self.conn.close()


if __name__ == '__main__':
    # os.system("ssh -L 3305:mysqlsrv1.cs.tau.ac.il:3306 amitmiara@nova.cs.tau.ac.il")

    dbq = DBQuery()
    dbq.get_most_popular_languages()
    dbq.get_avg_revenue_per_country()
    dbq.get_profitable_genre_by_country("Spain")
    dbq.get_popular_actors_by_genre("Adventure")
    dbq.get_roi_by_country_and_genre()
    dbq.get_roi_of_movie_compared_to_avg_roi()
    dbq.get_popularity_of_word_in_title_by_country("Harry")
    dbq.close_conn()



