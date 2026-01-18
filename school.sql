SELECT * FROM school_assignments;
SELECT * FROM school_results;
SELECT * FROM school_announcements;
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'assignments';
INSERT INTO assignments (title, description, due_date)
VALUES ('Math Homework', 'Algebra problems', '2026-01-15 10:00:00');
