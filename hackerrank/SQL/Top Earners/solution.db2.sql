SELECT months * salary AS earnings, COUNT(*) FROM employee GROUP BY months * salary ORDER BY earnings DESC FETCH FIRST 1 ROW ONLY;
