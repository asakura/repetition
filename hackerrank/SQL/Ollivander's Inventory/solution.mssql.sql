SELECT id, cheap.age, coins_needed, wa.power
FROM wands wa
JOIN (
  SELECT wa.code, power, MAX(wp.age) AS age, MIN(coins_needed) AS price
  FROM wands wa
  JOIN wands_property AS wp ON wp.code = wa.code
  WHERE wp.is_evil = 0
  GROUP BY wa.code, wa.power
) cheap ON cheap.code = wa.code AND cheap.price = wa.coins_needed
ORDER BY wa.power DESC, cheap.age DESC;
