SELECT G.away_team, G.home_team, G.season, G.week, G.away_points, G.home_points, G.away_post_win_prob AS prob, V.name as venue_name
FROM lironcohen3.games as G, lironcohen3.venues as V
WHERE G.venue_id = V.venue_id AND ( home_post_win_prob > away_post_win_prob AND home_points < away_points ) AND ( away_points - home_points > 10  AND away_post_win_prob < 0.4 ) 
UNION 
SELECT G.home_team, G.away_team, G.season, G.week, G.home_points, G.away_points, G.home_post_win_prob AS prob, V.name as venue_name
FROM lironcohen3.games as G, lironcohen3.venues as V
WHERE G.venue_id = V.venue_id AND ( G.home_post_win_prob < G.away_post_win_prob AND G.home_points > G.away_points ) AND ( G.home_points - G.away_points > 10 AND G.home_post_win_prob < 0.4)
ORDER BY prob

# Optimize by adding an index on home_post_win_prob and away_post_win_prob

# FROM lironcohen3.games as G
# WHERE ( home_post_win_prob > away_post_win_prob AND home_points < away_points ) AND ( away_points - home_points > 10 )