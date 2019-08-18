SELECT name || '(' || SUBSTR(occupation, 1, 1) || ')' FROM occupations ORDER BY name;
SELECT 'There are a total of ' || count(occupation) || ' ' || LOWER(occupation) || 's.'
FROM occupations
GROUP BY occupation
ORDER BY 1;
