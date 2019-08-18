SELECT su.hacker_id, ha.name
FROM submissions su
JOIN hackers ha ON ha.hacker_id = su.hacker_id
JOIN challenges ch ON ch.challenge_id = su.challenge_id
JOIN difficulty di ON di.difficulty_level = ch.difficulty_level
WHERE di.score = su.score
GROUP BY su.hacker_id, ha.name
HAVING COUNT(su.challenge_id) > 1
ORDER BY COUNT(su.challenge_id) DESC, hacker_id ASC;
