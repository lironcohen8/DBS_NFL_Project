SELECT team, stat_name, stat_value FROM lironcohen3.stats AS s
	WHERE team = "Miami"
	AND s.stat_value >= (SELECT AVG(s2.stat_value) AS average_value
						FROM lironcohen3.stats AS s2
						WHERE s.stat_name = s2.stat_name
						GROUP BY stat_name);