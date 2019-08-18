SELECT DISTINCT city
FROM station
WHERE SUBSTRING(LOWER(city), 1, 1) NOT IN ('a', 'e', 'i', 'o', 'u');
