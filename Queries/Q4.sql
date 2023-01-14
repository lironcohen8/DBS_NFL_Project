SELECT 
    v1.state, v1.name, v1.capacity
FROM
    lironcohen3.venues AS v1
WHERE
    v1.state <> ''
        AND v1.capacity >= ALL (SELECT v2.capacity
								FROM
									lironcohen3.venues AS v2
								WHERE
									v2.state = v1.state)


