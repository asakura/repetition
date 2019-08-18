SELECT *
FROM (
  SELECT months * salary AS earnings, COUNT(*) FROM employee GROUP BY months * salary ORDER BY earnings DESC
)
WHERE rownum <= 1;
