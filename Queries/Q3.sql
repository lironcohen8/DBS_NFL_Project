SELECT 
    s1.team, s1.stat_name, s1.stat_value
FROM
    lironcohen3.stats AS s1
WHERE
    s1.team = '{input_team_name}'
        AND s1.stat_value >= (SELECT AVG(s2.stat_value) AS average_value
								FROM
									lironcohen3.stats AS s2
								WHERE
									s1.stat_name = s2.stat_name
								GROUP BY s2.stat_name)


