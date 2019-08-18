SELECT DISTINCT city
FROM station
WHERE SUBSTR(LOWER(city), LENGTH(city), 1) NOT IN ('a', 'e', 'i', 'o', 'u');
