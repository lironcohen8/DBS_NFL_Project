SELECT 
    T.team_name,
    T.conference,
    T.mascot,
    T.twitter,
    V.name AS venue_name,
    SUM(DP.overall) AS sum_overall_draft
FROM
    lironcohen3.draft_picks AS DP,
    lironcohen3.teams AS T,
    lironcohen3.venues AS V
WHERE
    T.team_id = DP.college_id
    AND T.venue_id = V.venue_id
GROUP BY T.team_name , T.team_id
ORDER BY sum_overall_draft DESC
LIMIT 10


