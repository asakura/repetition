SELECT
  n,
  IF(
    p IS NULL,
    'Root',
    IF(
      (SELECT COUNT(*) FROM bst WHERE p = b.n)>1,
      'Inner',
      'Leaf'
    )
  )
FROM bst b
ORDER BY n;
