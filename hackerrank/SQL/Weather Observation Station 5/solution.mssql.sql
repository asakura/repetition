SELECT TOP 1 city, LEN(city)
FROM station
ORDER BY LEN(city), city;

SELECT TOP 1 city, LEN(city)
FROM station
ORDER BY LEN(city) DESC, city;
