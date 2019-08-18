SELECT
  co.company_code,
  co.founder,
  COUNT(DISTINCT lm.lead_manager_code),
  COUNT(DISTINCT sm.senior_manager_code),
  COUNT(DISTINCT ma.manager_code),
  COUNT(DISTINCT em.employee_code)
FROM
  company co,
  lead_manager lm,
  senior_manager sm,
  manager ma,
  employee em
WHERE
  co.company_code = lm.company_code
  AND lm.lead_manager_code = sm.lead_manager_code
  AND sm.senior_manager_code = ma.senior_manager_code
  AND ma.manager_code = em.manager_code
GROUP BY co.company_code, co.founder
ORDER BY co.company_code;
