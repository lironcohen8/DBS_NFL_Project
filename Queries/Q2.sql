SELECT 
    P.player_id, P.name, P.position, T.team_name,
    SUM(CASE WHEN G.home_points > G.away_points THEN 1
        ELSE 0 END) AS wins,
    SUM(CASE WHEN G.home_points = G.away_points THEN 1
        ELSE 0 END) AS ties,
    SUM(CASE WHEN G.home_points < G.away_points THEN 1
        ELSE 0 END) AS losses,
    AVG(P.first_down) AS avg_first_down,
    AVG(P.second_down) AS avg_second_down,
    AVG(P.third_down) AS avg_third_down
FROM
    lironcohen3.players AS P
        LEFT JOIN
    lironcohen3.teams AS T ON P.team = T.team_name
        LEFT JOIN
    lironcohen3.games AS G ON (G.home_id = T.team_id
        OR G.away_id = T.team_id)
WHERE
    P.position = '{input_position_abb}'
GROUP BY P.player_id
ORDER BY first_down DESC
LIMIT 50

