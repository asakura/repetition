SELECT *
FROM (SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city), city)
WHERE rownum <= 1;

SELECT *
FROM (SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city) DESC, city)
WHERE rownum <= 1;
