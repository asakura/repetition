SELECT TOP 1 CAST(ROUND(long_w, 4) AS DECIMAL(10, 4)) FROM station WHERE lat_n > 38.7780 ORDER BY lat_n;
