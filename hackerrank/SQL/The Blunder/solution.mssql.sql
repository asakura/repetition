SELECT
  CAST(
    CEILING(
      AVG(CAST(salary AS DECIMAL)) - AVG(CAST(REPLACE(salary, '0', '') AS DECIMAL))
    )
  AS INTEGER)
FROM employees;
