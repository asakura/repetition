SELECT CONCAT(name, "(", LEFT(occupation, 1), ")") FROM occupations ORDER BY name ASC;
SELECT
  CONCAT("There are a total of ", count(occupation), " ", LOWER(occupation), "s.")
FROM occupations
GROUP BY occupation
ORDER BY 1 ASC;
