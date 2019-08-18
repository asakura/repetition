SELECT ha.hacker_id, ha.name, COUNT(ch.challenge_id) AS total
FROM hackers ha
JOIN challenges ch ON ha.hacker_id = ch.hacker_id
GROUP BY ha.hacker_id, name
HAVING
  COUNT(ch.challenge_id) = (
    SELECT COUNT(challenge_id) as max_total
    FROM challenges
    GROUP BY hacker_id
    ORDER BY max_total DESC
    FETCH FIRST 1 ROWS ONLY
  )
  OR COUNT(ch.challenge_id) IN (
    SELECT total
    FROM (
      SELECT COUNT(challenge_id) AS total
      FROM hackers ha
      JOIN challenges ch ON ch.hacker_id = ha.hacker_id
      GROUP BY ha.hacker_id
    ) all_totals
    GROUP BY total
    HAVING COUNT(total) = 1
  )
ORDER BY total DESC, ha.hacker_id;
