SELECT
  ha.hacker_id,
  name,
  SUM(score.max) AS total
FROM hackers ha
JOIN (
  SELECT hacker_id, MAX(score) AS max FROM submissions GROUP BY challenge_id, hacker_id
) AS score ON score.hacker_id = ha.hacker_id
GROUP BY ha.hacker_id, name
HAVING SUM(score.max) > 0
ORDER BY total DESC, ha.hacker_id;
