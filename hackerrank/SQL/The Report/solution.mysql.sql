SELECT IF(gr.grade > 7, st.name, NULL), gr.grade, st.marks
FROM students st
JOIN grades AS gr ON st.marks BETWEEN gr.min_mark AND gr.max_mark
ORDER BY gr.grade DESC, st.name ASC;
