SELECT name FROM students WHERE marks > 75 ORDER BY SUBSTR(name, LENGTH(name) - 2, 3), id;
