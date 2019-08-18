SELECT CAST(ROUND(lat_n, 4) AS DECIMAL(10, 4))
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
FETCH FIRST 1 ROW ONLY;
