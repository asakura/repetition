SELECT DISTINCT city FROM station WHERE SUBSTR(LOWER(city), LENGTH(city), 1) IN ('a','e','i','o','u');