SET @row_id := -1;
SELECT
  ROUND(AVG(lat_n), 4)
FROM (
  SELECT
    @row_id := @row_id + 1 AS row_id,
    station.lat_n as lat_n
  FROM station
  ORDER BY station.lat_n
) as sub
WHERE sub.row_id IN (FLOOR(@row_id / 2), CEIL(@row_id / 2));
