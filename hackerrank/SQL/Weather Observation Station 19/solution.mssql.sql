SELECT
  CAST(
    ROUND(SQRT(POWER(MIN(lat_n) - MAX(lat_n), 2) + POWER(MIN(long_w) - MAX(long_w), 2)), 4)
    AS DECIMAL(10, 4)
  )
FROM station;
