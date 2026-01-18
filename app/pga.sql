INSERT INTO school_assignments (teacher_id, class, title, file_url, due_date)
VALUES ('T001', 'Form 5', 'Chemistry Notes', 'uploads/chemistry.pdf', '2025-01-15');

INSERT INTO school_results (student_id, term, subject, score, grade)
VALUES ('S001', 'Term1', 'Math', 85, 'A');

INSERT INTO announcements (title, body, audience, created_by)
VALUES ('Exam Schedule', 'Midterm exams start next week', 'ALL', 'Admin');