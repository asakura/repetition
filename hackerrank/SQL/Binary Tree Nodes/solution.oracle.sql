SELECT
  n,
  CASE
    WHEN p IS NULL THEN 'Root'
    WHEN (SELECT COUNT(*) FROM bst WHERE p = b.n) > 1 THEN 'Inner'
    ELSE 'Leaf'
  END
FROM bst b
ORDER BY n;
