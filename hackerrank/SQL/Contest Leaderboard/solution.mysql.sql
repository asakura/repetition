SELECT
  hackers.hacker_id,
  name,
  SUM(score.max) AS total
FROM hackers
JOIN (
  SELECT hacker_id, MAX(score) AS max FROM submissions GROUP BY challenge_id, hacker_id
) AS score ON score.hacker_id = hackers.hacker_id
GROUP BY hacker_id, name
HAVING total > 0
ORDER BY total DESC, hacker_id ASC;
