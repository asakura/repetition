SELECT
  CAST(
    CEIL(
      AVG(CAST(salary AS DECIMAL)) - AVG(REPLACE(salary, '0', ''))
    )
  AS INTEGER)
FROM employees;
