SELECT DISTINCT city
FROM station
WHERE
  SUBSTRING(LOWER(city), 1, 1) IN ('a','e','i','o','u')
  AND SUBSTRING(LOWER(city), LEN(city), 1) IN ('a','e','i','o','u');
