SELECT TOP 1 months * salary AS earnings, COUNT(*) FROM employee GROUP BY months * salary ORDER BY earnings DESC;
