SELECT CASE WHEN gr.grade > 7 THEN st.name ELSE 'NULL' END, gr.grade, st.marks
FROM students st
JOIN grades AS gr ON st.marks BETWEEN gr.min_mark AND gr.max_mark
ORDER BY gr.grade DESC, st.name;
