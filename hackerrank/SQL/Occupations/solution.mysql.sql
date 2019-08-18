SET @doctor=0, @actor=0, @singer=0, @professor=0;
SELECT MIN(doctor), MIN(professor), MIN(singer), MIN(actor)
FROM (
  SELECT
    CASE
      WHEN occupation = 'Doctor' THEN (@doctor := @doctor + 1)
      WHEN occupation = 'Professor' THEN (@professor := @professor + 1)
      WHEN occupation = 'Singer' THEN (@singer := @singer + 1)
      WHEN occupation = 'Actor' THEN (@actor := @actor + 1)
    END AS row_id,
    CASE WHEN occupation = 'Doctor' THEN name END AS doctor,
    CASE WHEN occupation = 'Professor' THEN name END AS professor,
    CASE WHEN occupation = 'Singer' THEN name END AS singer,
    CASE WHEN occupation = 'Actor' THEN name END AS actor
  FROM occupations
  ORDER BY name
) sparse
GROUP BY sparse.row_id;
