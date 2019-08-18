SET @counter := 21;

SELECT REPEAT('* ', @counter := @counter - 1) FROM information_schema.tables;
