SELECT 
    T1.team_name AS home_team,
    T2.team_name as away_team,
    G.season,
    G.week,
    G.away_points,
    G.home_points,
    G.away_post_win_prob AS prob,
    V.name as venue_name
FROM
    lironcohen3.games as G,
    lironcohen3.venues as V,
    lironcohen3.teams as T1,
    lironcohen3.teams as T2
WHERE
    (G.venue_id = V.venue_id
        AND G.home_id = T1.team_id
        AND G.away_id = T2.team_id)
        AND (G.home_post_win_prob > G.away_post_win_prob
        AND G.home_points < G.away_points)
        AND (G.away_points - G.home_points > 10
        AND G.away_post_win_prob < 0.4) 
UNION SELECT 
    T1.team_name AS home_team,
    T2.team_name as away_team,
    G.season,
    G.week,
    G.away_points,
    G.home_points,
    G.away_post_win_prob AS prob,
    V.name as venue_name
FROM
    lironcohen3.games as G,
    lironcohen3.venues as V,
    lironcohen3.teams as T1,
    lironcohen3.teams as T2
WHERE
    (G.venue_id = V.venue_id
        AND G.home_id = T1.team_id
        AND G.away_id = T2.team_id)
        AND (G.home_post_win_prob < G.away_post_win_prob
        AND G.home_points > G.away_points)
        AND (G.home_points - G.away_points > 10
        AND G.home_post_win_prob < 0.4)
ORDER BY prob