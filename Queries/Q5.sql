# convertion rate from pound to kg is 0.0254
# convertion rate from inch to meter is 0.4535

SELECT 
    Dpos.position_name,
    Dpos.abbreviation,
    MIN(Dpick.height) * 0.0254 AS min_height_meter,
    MAX(Dpick.height) * 0.0254 AS max_height_meter,
    MIN(Dpick.weight) * 0.4535 AS min_weight,
    MAX(Dpick.weight) * 0.4535 AS max_weight
FROM
    lironcohen3.draft_picks AS Dpick,
    lironcohen3.draft_teams AS DT,
    lironcohen3.draft_positions AS Dpos
WHERE
    DT.location = Dpick.nfl_team
    AND Dpos.position_name = Dpick.position
GROUP BY Dpos.position_name


