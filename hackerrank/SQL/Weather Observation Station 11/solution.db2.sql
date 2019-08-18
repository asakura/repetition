SELECT DISTINCT city
FROM station
WHERE
  SUBSTR(LOWER(city), 1, 1) NOT IN ('a','e','i','o','u')
  OR SUBSTR(LOWER(city), LENGTH(city), 1) NOT IN ('a','e','i','o','u');
