-- Table for uploaded assignments
CREATE TABLE school_assignments (
  id SERIAL PRIMARY KEY,
  teacher_id VARCHAR(50),
  class VARCHAR(50),
  title VARCHAR(100),
  file_url TEXT,
  due_date DATE
);

-- Table for student results
CREATE TABLE school_results (
  id SERIAL PRIMARY KEY,
  student_id VARCHAR(50),
  term VARCHAR(20),
  subject VARCHAR(50),
  score INT,
  grade VARCHAR(2)
);

-- Table for school-wide announcements
CREATE TABLE announcements (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  body TEXT,
  audience VARCHAR(50),
  created_by VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO school_assignments (teacher_id, class, title, file_url, due_date)
VALUES ('T001', 'Form 5', 'Chemistry Notes', 'uploads/chemistry.pdf', '2025-01-15');

INSERT INTO school_results (student_id, term, subject, score, grade)
VALUES ('S001', 'Term1', 'Math', 85, 'A');

INSERT INTO announcements (title, body, audience, created_by, created_at)
VALUES ( 'Chemistry notes', 'Atom','Students', 'Admin', '2025-01-09');